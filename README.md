**ECMS - Email Campaign Management System**
---------------------------------------

**Project Overview**

The Email Campaign Management System (ECMS) is a web-based application developed using the Django framework that allows users to create, schedule, and manage bulk email campaigns efficiently.

The system enables administrators to upload recipient lists through CSV files, schedule campaigns for future delivery, and automatically send emails using an SMTP mail server. It also tracks delivery status for each email and provides a dashboard to monitor campaign progress in real time.

This project demonstrates backend development, database management, email automation, scheduling mechanisms, and reporting capabilities.

**Key Features**
1. Campaign Management

Create and schedule email campaigns.

Define campaign name, subject, content, and scheduled sending time.

Track campaign status (Scheduled, Running, Completed).

**2. Recipient Management**

Upload recipient lists using CSV files.

Automatically store recipient details in the database.

Validate and manage subscriber email addresses.

**3. Automated Email Scheduling**

Emails are automatically sent when the scheduled time is reached.

Uses SMTP configuration for email delivery.

No manual intervention required.

**4. Campaign Dashboard**

Displays all campaigns with key metrics:

Total Recipients

Emails Sent

Failed Emails

Campaign Status

Allows users to view detailed delivery logs.

**5. Delivery Logging**

Tracks the status of each email delivery.

Logs include:

Recipient email

Delivery status

Failure reason (if any)

**Timestamp**

6. Campaign Reporting

After campaign completion, a CSV summary report is generated.

The report includes delivery statistics and email status.

The report is automatically emailed to the administrator.

**7. Campaign Control**

View campaign details and delivery logs.

Delete campaigns from the dashboard.

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
