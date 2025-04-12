# ⛅ Django Weather App

A simple Django application that fetches real-time weather data from the OpenWeatherMap API based on the user's city input.

## 🌦 Features

- City-wise weather forecast
- Displays:
  - Temperature 🌡️
  - Pressure ⬇️
  - Humidity 💧
  - Wind Speed 🌬️
- Simple and clean UI

## 🛠 Tech Stack

- Django (Python Web Framework)
- OpenWeatherMap API
- HTML/CSS (for templates)

## 🚀 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Abinanthanan08/django-weather-app.git
   cd django-weather-app

2.Create a virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate


3.Install the required packages
pip install -r requirements.txt

4.Run database migrations (if any)
python manage.py migrate

5.Start the development server
python manage.py runserver and open http://127.0.0.1:8000/ in your browser
