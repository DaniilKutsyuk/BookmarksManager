# Bookmarks Manager

This is a Django-based Bookmarks Manager project that allows users to save, categorize, and manage their bookmarks (URLs). It includes user authentication (register, login, logout), CRUD operations for bookmarks, and the ability to categorize bookmarks.

## Features

- User Registration and Authentication (JWT)
- Add, Edit, Delete, and List Bookmarks
- Categorize Bookmarks
- Mark Bookmarks as Favorite
- REST API for interacting with bookmarks

## Prerequisites

Make sure you have the following installed:

- Python 3.8 or later
- Django 4.x or later
- PostgreSQL (or any other database of your choice)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bookmarks_manager.git
   cd bookmarks_manager
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
4. Set up the database:
   ```bash
   python manage.py migrate
5. Create a superuser to access the admin interface:
   ```bash
   python manage.py createsuperuser
6. Run the development server:
   ```bash
   python manage.py runserver
7. Visit http://127.0.0.1:8000/ in your browser.
