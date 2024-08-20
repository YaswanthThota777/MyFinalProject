from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import numpy as np
import pretty_midi
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os
from django.conf import settings
from tensorflow.keras.models import load_model
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm
from django.contrib.auth import logout
from .models import MusicFile 
from django.core.files import File


def generate_music(request):
    if request.method == 'POST':
        regenerate = request.POST.get('regenerate').strip().lower()
        if regenerate == 'yes':
            try:
                seed_sequence = [60, 62, 64, 65, 67]
                sequence_length = 50
                generated_notes = generate_sequence(model, seed_sequence, num_notes=100, sequence_length=sequence_length)
                midi_file_path = os.path.join(settings.MEDIA_ROOT, 'generated_music.mid')
                wav_file_path = os.path.join(settings.MEDIA_ROOT, 'generated_music.wav')

                save_sequence_to_midi(generated_notes, midi_file_path)
                midi_to_wav(midi_file_path, wav_file_path)

                audio_file_path = os.path.join(settings.MEDIA_URL, 'generated_music.wav')
                return render(request, 'generator/generate_music.html', {'audio_file': audio_file_path, 'midi_file_path': midi_file_path})

            except Exception as e:
                return render(request, 'generator/generate_music.html', {'error': str(e)})

        elif regenerate == 'no':
            return render(request, 'generator/generate_music.html', {'message': 'No music generated.'})

        else:
            return render(request, 'generator/generate_music.html', {'error': 'Invalid input. Please type "yes" or "no".'})

    return render(request, 'generator/generate_music.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = SignUpForm()
    return render(request, 'generator/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = LoginForm()
    return render(request, 'generator/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home') 

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def contact(request):
    return render(request, 'generator/contact.html')

def privacy_policy(request):
    return render(request, 'generator/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'generator/terms_of_service.html')


model = load_model(r'C:\Users\yaswa\Downloads\music\music_generator\generator\piano_model.h5')


def generate_sequence(model, seed_sequence, num_notes, sequence_length, temperature=1.0):
    generated_sequence = seed_sequence.copy()

    for _ in range(num_notes):
        padded_sequence = pad_sequences([generated_sequence], maxlen=sequence_length, padding='pre', truncating='pre')
        predicted_probs = model.predict(padded_sequence, verbose=0)[0, -1]

        predicted_probs = np.exp(np.log(predicted_probs) / temperature)
        predicted_probs /= np.sum(predicted_probs)

        predicted_note = np.random.choice(range(len(predicted_probs)), p=predicted_probs)
        generated_sequence.append(predicted_note)
        generated_sequence = generated_sequence[-sequence_length:]

    return generated_sequence

def save_sequence_to_midi(generated_notes, file_name='generated_music.mid'):
    midi_data = pretty_midi.PrettyMIDI()
    piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
    piano = pretty_midi.Instrument(program=piano_program)

    note_duration = 0.5
    start_time = 0.0

    for note in generated_notes:
        midi_note = pretty_midi.Note(
            velocity=100,
            pitch=note,
            start=start_time,
            end=start_time + note_duration
        )
        piano.notes.append(midi_note)
        start_time += note_duration

    midi_data.instruments.append(piano)
    midi_data.write(file_name)

def midi_to_wav(midi_file, output_wav):
    os.system(f'timidity {midi_file} -Ow -o {output_wav}')


