# Supermarket Stock Management System

This is a Django-based web application for managing the stock of products in a supermarket. It allows managers to handle suppliers, products, stock transactions, and user profiles.

## Features

- Supplier management: Add, edit, and delete supplier details.
- Product management: Add, edit, and delete products, including their price, quantity, and expiry date.
- Stock transactions: Track sales, purchases, and returns of products.
- User profiles: Each user has a profile with their image, bio, address, and phone number.
- Authentication: User registration, login, and profile management.
- Role management: Separate views for managers and cashiers, with appropriate permissions for each role.

## Prerequisites

To run this project, you'll need the following installed on your system:

- Python 3.x
- Django 3.x or later
- PostgreSQL or SQLite (or any preferred database)
- Git

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/supermarket-stock-management.git
cd supermarket-stock-management
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Windows
venv\Scripts\activate

# For macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
#Run the following commands to create the database tables:
python manage.py migrate
#Create a superuser to access the admin panel by running:
python manage.py createsuperuser
#Start the Django development server using
python manage.py runserver
#project structure
supermarket-stock-management/
│
├── inventory/                  # Main app for the stock management system
│   ├── migrations/             # Database migration files
│   ├── templates/              # HTML templates for the app
│   ├── static/                 # Static files (CSS, JS, images)
│   ├── views.py                # Handles views and logic
│   ├── models.py               # Database models for the system
│   ├── forms.py                # Forms for user input
│   └── urls.py                 # URL routing for the app
│
├── users/                      # App for user management and profiles
│   ├── views.py                # Profile-related views
│   ├── forms.py                # Profile and user forms
│   └── signals.py              # Handles auto-creation of profiles
│
├── supermarket/                # Project-level settings
│   ├── settings.py             # Django settings (database, apps, middleware)
│   ├── urls.py                 # Project-wide URL routing
│
├── manage.py                   # Django management commands
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies

