**ECMS - Email Campaign Management System**
---------------------------------------

This project is developed using Django.

**Features**
--------
- Upload recipients via CSV
- Schedule email campaigns
- Automatic email sending via SMTP
- Campaign dashboard with progress tracking
- Delivery logs
- Campaign report generation (CSV)
- Automatic report email to admin

**Project Requirements**
--------------------
Python 3.10+
Django 4+
SMTP email configuration

**Setup Instructions**
------------------

1. Clone the repository

git clone https://github.com/indranilsahaedu/ColgenaiTask.git

2. Navigate to project folder

cd DjangoSample

3. Create virtual environment

python -m venv env

4. Activate virtual environment

Windows:
env\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

6. Apply migrations

python manage.py makemigrations
python manage.py migrate

7. Create admin user

python manage.py createsuperuser

8. Run the server

python manage.py runserver

Open in browser:

http://127.0.0.1:8000

Admin Panel:

http://127.0.0.1:8000/admin

**Email Configuration**
-------------------

Update settings.py If you want:

EMAIL_HOST = smtp.gmail.com
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = your_email@gmail.com
EMAIL_HOST_PASSWORD = your_app_password

CSV Format
----------

name,email

Rahul,rahul@gmail.com
Amit,amit@gmail.com
Priya,priya@gmail.com
