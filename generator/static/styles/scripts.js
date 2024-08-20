document.addEventListener('DOMContentLoaded', function() {
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const closeBtn = document.querySelector('.close-btn');
    const navbar = document.querySelector('.navbar');
    const navbarOverlay = document.querySelector('.navbar-overlay');
    const generateButton = document.getElementById('generate-music');
    const audioPlayer = document.getElementById('audio-player');
    const playButton = document.getElementById('play');
    const pauseButton = document.getElementById('pause');
    let audioElement = new Audio(); 

    hamburgerMenu.addEventListener('click', function() {
        navbar.classList.add('active');
        navbarOverlay.classList.add('active');
        hamburgerMenu.style.display = 'none'; 
        closeBtn.style.display = 'block'; 
    });

    closeBtn.addEventListener('click', function() {
        navbar.classList.remove('active');
        navbarOverlay.classList.remove('active');
        hamburgerMenu.style.display = 'block'; 
        closeBtn.style.display = 'none'; 
    });

    navbarOverlay.addEventListener('click', function() {
        navbar.classList.remove('active');
        navbarOverlay.classList.remove('active');
        hamburgerMenu.style.display = 'block'; 
        closeBtn.style.display = 'none'; 
    });

    generateButton.addEventListener('click', function() {
        fetch('/generate-music/')
            .then(response => response.json())
            .then(data => {
                audioElement.src = data.audio_url; 
                audioElement.load();
                audioElement.play();
            })
            .catch(error => console.error('Error generating music:', error));
    });

    playButton.addEventListener('click', function() {
        audioElement.play();
    });

    pauseButton.addEventListener('click', function() {
        audioElement.pause();
    });
});

function selectButton(button) {
    document.querySelectorAll('.genre-button').forEach(btn => btn.classList.remove('selected'));
    button.classList.add('selected');
}