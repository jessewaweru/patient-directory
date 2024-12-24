# Patient Directory

## Project Description
Patient Directory is a Django-based web application that allows users to register, log in, and manage patient profiles. 
It features secure authentication, profile management, and a registration system.

## Installation

### Prerequisites

Before setting up the project, ensure you have the following installed:

- Python 3.8+ (preferably the latest stable release)
- `pip` (Python package installer)
- `virtualenv` (for creating isolated environments)

## Setup Steps
1. Clone the repository

``` bash
git clone https://github.com/yourusername/patient-directory.git
cd patient-directory

```
2. Set up a virtual environment
``` bash
python3 -m venv venv
source venv/bin/activate

```
3. Install the dependencies as referenced below using a requirements text file.
```bash
pip install -r requirements.txt

```
4. Set up a Postgres database
- Ensure the psycopg2 library is installed from the dependencies list.
- Then proceed to set up the database settings as follows,

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',  # Use the actual host if it's remote
        'PORT': '5432',       # Default PostgreSQL port
    }
}

```
5. Run the development server
```bash
python manage.py runserver

```

## Dependencies
This project relies on the following major dependencies:

Django: A high-level Python web framework that simplifies web development.

- Installation: pip install django

Django REST Framework (DRF): A powerful toolkit for building Web APIs.

- Installation: pip install djangorestframework

Django-crispy-forms: For better form rendering and handling.

- Installation: pip install django-crispy-forms

Requests: A simple HTTP library to make requests to external APIs (if needed).

- Installation: pip install requests

Python-dotenv: For managing environment variables.

- Installation: pip install python-dotenv

## Usage
- Register a New Patient: Navigate to /register/ to create a new patient profile.
- Login: Use the /login/ endpoint to log into the system and obtain a JWT token.
- Access Patient Profiles: After logging in, users can view and edit their profiles.

Some of the api endpoints derived from the project include the following:

- POST /api/register/: Register a new patient by providing necessary data in the request body.
- POST /api/login/: Log in by providing valid credentials, and receive a JWT token.
- POST /api/lsuccess/: A page comfirming the successfull login of a user after they have been redirected.

## Features
- User Authentication: Secure login and registration with token authentication.
- Patient Profile Management: Users can create, view, and update their profiles.
- Django Admin Interface: For managing patient data and users.
- REST API: Endpoints for patient registration, login, and profile management.

