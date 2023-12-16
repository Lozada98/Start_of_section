Project Summary

This project is a Registration and Login application developed in Python using the Flask framework. The application allows users to register, log in, and access a protected page once authenticated. Here is a summary of the project structure and how it works:
Project Structure

    .api: Folder containing the main file of the application.
        app.py: Main file of the Flask application.

    .database: Folder storing the JSON file used as a database.
        base_de_datos.json: JSON file to store user credentials.

    .static: Folder containing static files such as style sheets.
        styles.css: CSS file defining the style of the interface.

    .templates: Folder containing HTML files for web pages.
        index.html: Main page with the login form.
        registro.html: Registration page with the account creation form.

    requirements.txt: File listing dependencies needed to run the application.

    vercel.json: Configuration file for Vercel, a continuous deployment service.

Key Features

    Login:
        Users can enter their email and password to log in.
        Credentials are verified against the database stored in a JSON file.

    Registration:
        New users can register by providing an email and password.
        It checks if the email is already registered before storing the credentials.

    Protected Page:
        After successfully logging in, users are redirected to a protected page.
        The page includes a welcome message and a link to a YouTube video.

    Style and Social Media:
        Page design is enhanced with a CSS style file.
        Links to social media profiles (Instagram, GitHub, LinkedIn) are included.

Deployment on Heroku

The project has already been deployed on Heroku, and it can be accessed through the following URL: https//..