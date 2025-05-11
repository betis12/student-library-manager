# Student Library Manager (CLI & Web)

A Python application for managing student and library records with both a command-line interface (CLI) and a Flask-based web interface.

## 🔹 Features

- Add, update, search, and delete student profiles
- CLI version using `rich` for styled terminal output
- Web version using Flask, Bootstrap, and HTML templates
- Data persistence via `pickle` (CLI) and `SQLite` (Web)
- Object-oriented and modular code design

## 📂 Structure

```
student-library-manager/
├── CLI/
│   ├── menu.py
│   └── studentOperation.py
├── Web/
│   ├── app.py
│   ├── Book.py
│   ├── requirements.txt
```

## ⚙️ Requirements (Web)

Install dependencies for the Flask version:

```bash
pip install -r Web/requirements.txt
```

## ▶️ Run the Web App

```bash
cd Web
python app.py
```

## 📜 License

This project is released under the MIT License.
