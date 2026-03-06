# Django Mail Sender

A Django-based web application for sending emails via SMTP. The project includes two versions: a simple mailer for basic email sending, and an advanced mailer with additional features such as file attachments, CC/BCC support, email templates, and a sent history log.

Both versions implement the **Post/Redirect/Get (PRG)** design pattern to prevent duplicate form submissions on page refresh.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [PRG Pattern](#prg-pattern)
- [Technologies Used](#technologies-used)

---

## Features

### Simple Mailer (`/`)
- Send emails with a recipient address, subject, and message body
- Clean, responsive UI with glassmorphism design
- PRG pattern to prevent duplicate submissions

### Advanced Mailer (`/advanced/`)
- All features of the simple mailer, plus:
- **File Attachments** -- Upload and attach files to outgoing emails
- **CC and BCC** -- Send copies to multiple recipients via comma-separated addresses
- **Email Templates** -- Pre-defined templates that auto-fill the subject and message fields
- **Sent History** -- A log of all sent emails with status tracking (Success/Failed), accessible at `/advanced/history/`
- Dark-themed UI with glassmorphism design

---

## Project Structure

```
DjangoMailSender/
|-- mail_project/          # Django project configuration
|   |-- settings.py        # Project settings (SMTP config, installed apps)
|   |-- urls.py            # Root URL routing
|   |-- wsgi.py
|   |-- asgi.py
|
|-- mailer/                # Simple mailer app
|   |-- views.py           # Form display and email sending logic
|   |-- forms.py           # Email form (To, Subject, Message)
|   |-- urls.py            # Routes: /, /success/
|   |-- templates/mailer/  # HTML templates (form, success page)
|
|-- advanced_mailer/       # Advanced mailer app
|   |-- models.py          # EmailTemplate and SentEmail models
|   |-- views.py           # Email sending with attachments, CC/BCC, history
|   |-- forms.py           # Extended form (To, CC, BCC, Subject, Message, Attachment, Template)
|   |-- admin.py           # Admin panel registration for models
|   |-- urls.py            # Routes: /, /success/, /history/, /api/template/<id>/
|   |-- templates/advanced_mailer/  # HTML templates (form, success, history)
|
|-- .env                   # Email credentials (not tracked in git)
|-- .gitignore
|-- manage.py
|-- README.md
```

---

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- A Gmail account with an App Password (or any other SMTP provider)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/NeerajBarhate23/DjangoMailSender.git
   cd DjangoMailSender
   ```

2. **Install dependencies**

   ```bash
   pip install django python-dotenv
   ```

3. **Run database migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser** (required for managing email templates via the admin panel)

   ```bash
   python manage.py createsuperuser
   ```

---

## Configuration

Create a `.env` file in the project root directory with your SMTP credentials:

```
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

### Generating a Gmail App Password

1. Go to your Google Account settings.
2. Navigate to Security and enable 2-Step Verification.
3. Under "App passwords", generate a new password for "Mail".
4. Copy the 16-character password into the `.env` file.

The application reads these values securely using `python-dotenv`. The `.env` file is listed in `.gitignore` and will not be pushed to version control.

---

## Usage

1. **Start the development server**

   ```bash
   python manage.py runserver
   ```

2. **Access the application**

   | Page              | URL                                      |
   |-------------------|------------------------------------------|
   | Simple Mailer     | http://127.0.0.1:8000/                   |
   | Advanced Mailer   | http://127.0.0.1:8000/advanced/          |
   | Sent History      | http://127.0.0.1:8000/advanced/history/  |
   | Admin Panel       | http://127.0.0.1:8000/admin/             |

3. **Managing Email Templates**

   Log in to the Django Admin panel, navigate to "Email templates", and create templates with a name, subject, and message body. These templates will appear in the dropdown on the Advanced Mailer form and auto-fill the subject and message fields when selected.

---

## PRG Pattern

Both mailer apps implement the Post/Redirect/Get pattern:

1. **Post** -- The user submits the email form via a POST request.
2. **Redirect** -- After processing the email, the server responds with an HTTP 302 redirect to the success page.
3. **Get** -- The browser follows the redirect and loads the success page via a GET request.

This ensures that refreshing the success page does not trigger a duplicate email submission.

---

## Technologies Used

| Component       | Technology                        |
|-----------------|-----------------------------------|
| Backend         | Django 6.0, Python 3.x           |
| Email           | Django SMTP EmailBackend          |
| Frontend        | HTML, Tailwind CSS (CDN), JavaScript |
| Database        | SQLite                            |
| Font            | Inter (Google Fonts)              |
| Configuration   | python-dotenv                     |
