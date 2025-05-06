# Event Management Web Application

A Flask-based web application for managing events, built as part of a web development project.

## 🚀 Features

- User authentication (login/logout)
- Event registration
- Database integration using SQLAlchemy
- Database migrations using Flask-Migrate
- Bootstrap-styled frontend

## 🏗️ Tech Stack

- Python 3.13
- Flask 3.1
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite (or another database backend)

## 📝 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/hemantbansal230/Flask.git
   cd Flask
    ```
   
2. Create a virtual environment:
 ```bash
python -m venv virtual
source virtual/Scripts/activate  # on Windows
 ```

3. Install dependencies:
 ```bash
pip install -r requirements.txt
 ```

4. Set environment variables:
 ```bash
export FLASK_APP=main.py
export FLASK_ENV=development
 ```

5. Run the application:
 ```bash
flask run
 ```

6. Open http://127.0.0.1:5000/ in your browser.
