# Project TODO List

This is a simple cross-platform Todo List web application built with Flask and SQLite.

## Features

- Add, complete, and delete tasks
- Data stored locally using SQLite
- Minimal Bootstrap-based UI

## Requirements

- Python 3.8+
- pip

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python run.py
```

Open `http://localhost:5000` in your browser to use the application.

## Production readiness

For a production deployment, you can run the app using a WSGI server such as `gunicorn`:

```bash
pip install gunicorn
export FLASK_APP=app.routes:app
gunicorn -w 4 -b 0.0.0.0:8000 app.routes:app
```

This will serve the application on port 8000 using 4 worker processes.
