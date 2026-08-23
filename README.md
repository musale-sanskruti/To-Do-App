# To-Do App

A simple full-stack task manager built with Flask. Users can log in, add tasks, move them through status stages (Pending → Working → Completed), and delete tasks.

## Features

- User authentication with session-based login
- Add new tasks
- Update task status with a single click (Pending → Working → Completed)
- Delete individual tasks
- Flash messages for user feedback (success/warning alerts)
- Clean, responsive UI styled with custom CSS

## Tech Stack

- **Backend:** Python, Flask, Flask Blueprints
- **Database:** SQLAlchemy (SQLite by default)
- **Frontend:** Jinja2 templates, HTML, CSS
- **Auth:** Flask sessions

## Project Structure

```
todo_app/
├── app/
│   ├── __init__.py       # App factory, extensions setup
│   ├── models.py         # Task database model
│   ├── auth.py           # Login/logout routes
│   ├── tasks.py           # Task CRUD routes
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   └── tasks.html
│   └── static/
│       └── style.css
├── requirements.txt
├── run.py                # App entry point
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/todo_app.git
cd todo_app
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python run.py
```

The app will be available at `http://127.0.0.1:5000/`.

## Usage

1. Log in with your credentials
2. Add a new task using the input field
3. Click **Next** to move a task through its status stages
4. Click **Delete** to remove a task

## Future Improvements

- Add user registration
- Per-user task lists instead of a shared list
- Input validation and better error handling
- Deploy to a live hosting platform

## License

This project is open source and available under the [MIT License](LICENSE).