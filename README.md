# 🌐 Translation Web App
A simple **Flask-based web application** that translates text between different languages.  
The app provides a user-friendly interface to input text, choose a language, and view the translated result.

---

## 📂 Project Structure
├── app.py # Main Flask application
├── templates/
│ ├── index.html # Home page with input form
│ ├── result.html # Result page to display translation
├── static/
│ ├── css/
│ │ ├── index.css # Styles for home page
│ │ ├── result.css # Styles for result page

## 🚀 Features
- Translate text into multiple languages  
- Simple and clean web interface  
- Flask-powered backend

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/translation-app.git
   cd translation-app

2.**Create a virtual environment (optional but recommended)**
python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows

3.**Install dependencies**
pip install flask
pip install googletrans==4.0.0-rc1

4.**Run the app**
python app.py
Open in browser **http://127.0.0.1:5000/**
