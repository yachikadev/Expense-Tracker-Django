# Expense Tracker — Django

A web-based expense tracking application built with Django. Users can add, view, and manage their daily expenses through a clean, template-driven interface.

## Features

- Add and categorize expenses
- View expense history
- Image upload support (via Pillow)
- Django admin panel for data management

## Tech Stack

- **Backend:** Django 6.0.5
- **Language:** Python
- **Database:** PostgreSQL
- **Image Handling:** Pillow

## Project Structure
Expense-Tracker-Django/
├── ExpenseTracker/     # Main Django app
├── mysite/             # Project settings and URLs
├── templates/          # HTML templates
├── manage.py
└── requirements.txt

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- PostgreSQL

### Installation

```bash
git clone https://github.com/yachikadev/Expense-Tracker-Django.git
cd Expense-Tracker-Django

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Database Setup

```bash
psql -U postgres -c "CREATE DATABASE expense_tracker;"
```

Create a `.env` file in the project root:
DB_NAME=expense_tracker
DB_USER=postgres
DB_PASSWORD=your_password

### Run

```bash
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000` in your browser.

## Author

**Yachika Sharma** — [GitHub](https://github.com/yachikadev)