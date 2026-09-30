# Pet Adoption & Rescue Platform

A Django-based web application for browsing pets, submitting adoption requests, and managing pet adoption workflows.

The project includes both a Django template-based web application and a REST API built with Django REST Framework.

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Bootstrap 5
- HTML5
- CSS3
- JavaScript

## Planned Features

- User registration and authentication
- Pet browsing
- Pet search and filtering
- Pet details
- Adoption requests
- User adoption dashboard
- Favorites
- Pagination
- Django Admin management
- REST API
- Token authentication
- API search and filtering
- API pagination
- Business-rule validation
- Automated tests

## Project Status

Currently under development.

## Local Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd pet-adoption-platform

```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/Scripts/activate

```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Configure environment variables

```
Create a .env file based on .env.example.

```

### 5. Create the PostgreSQL database
Create a PostgreSQL database named:
```Plain text
pet_adoption_db

```

### 6. Run migrations

```bash
python manage.py migrate

```

### 7. Create a superuser

```bash
python manage.py createsuperuser

```

### 8. Start the development server

```bash
python manage.py runserver

```

## License

This project is developed for educational and portfolio purposes.

---
