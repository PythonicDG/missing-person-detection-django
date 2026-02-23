# Missing Person Detection System

A Django-based web application designed to help find missing persons by allowing users to report missing individuals, found persons, and communicate through a built-in messaging system.

## 🚀 Features

- **Reporting**: Report missing or found persons with photos and details.
- **Matching**: Automated face detection and matching (face embeddings).
- **Messaging**: Built-in chat system for users to communicate regarding leads.
- **User Profiles**: Manage personal information and contact details.

## 🛠️ Tech Stack

- **Backend**: Django 5.2 (Python)
- **Database**: SQLite 3
- **Frontend**: HTML5, CSS (Vanilla), JavaScript

## 🔧 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd "missing person detection django"
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   # Activate on Windows:
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Server**:
   ```bash
   python manage.py runserver
   ```

Open `http://127.0.0.1:8000` in your browser.

## 📁 Project Structure

- `accounts/`: Core logic for users, missing persons, and messaging.
- `pages/`: Templates and views for the landing pages.
- `core/`: Common utilities and shared components.

---
*Created for the Missing Person Detection Project.*
