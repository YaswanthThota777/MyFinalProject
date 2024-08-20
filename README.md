# MyFinalProject

## Distinctiveness and Complexity

This project, named "Emotion-Based Music Generator," is designed to be a unique and complex web application. Unlike typical e-commerce or social networking sites, this project allows users to generate music sequences based on specific emotions. The project utilizes Django for the backend, including a model that stores user preferences and generated music data. JavaScript is employed on the frontend to handle user interactions and dynamically update the page without requiring a reload.

The complexity arises from integrating multiple technologies to process MIDI files, converting them into audio formats, and providing an intuitive interface for users to interact with. The project also ensures mobile responsiveness, offering a seamless experience across different devices.

## File Contents

- **/media/**: Contains the generated audio files.
- **/static/**: Includes all static files such as CSS, JavaScript, and images.
  - **/css/styles.css**: Contains all the styles for the website.
  - **/js/scripts.js**: Manages the frontend logic and dynamic content.
  - **/images/logo.png**: The logo of the project.
- **/templates/**: Contains the HTML templates for the project.
  - **layout.html**: The base template extended by other pages.
  - **generate_music.html**: The main interface where users can generate music.
- **/generator/**: Django app that handles the core functionality.
  - **migrations/**: Directory containing database migration files.
  - **models.py**: Defines the database schema for the project.
  - **views.py**: Contains the views that manage the logic for generating music and rendering pages.
  - **urls.py**: Maps URLs to views in the `generator` app.
  - **forms.py**: Manages the forms for user inputs.
- **manage.py**: The entry point for running Django commands.
- **db.sqlite3**: The SQLite database file storing project data.
- **requirements.txt**: Lists all the Python packages required to run the project.
- **README.md**: This file, providing an overview and documentation of the project.

## How to Run the Application

To run this application on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com//MyFinalProject.git
   cd MyFinalProject
