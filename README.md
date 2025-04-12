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

## 💻 How to Run the Application

### 1. Clone the repository
```bash
git clone https://github.com/Abinanthanan08/Django-weather-app.git
cd weather-app
```
### 2.Set up a virtual environment
```bash
python3 -m venv venv
```
### 3.Activate the virtual environment
```bash
venv\Scripts\activate
```
### 4.Install the required dependencies
```bash
pip install -r requirements.txt
```
### 5.Set up the OpenWeatherMap API
Go to OpenWeatherMap and sign up for an API key.
In the Django project, create a .env file or directly update settings.py to store your OpenWeatherMap API key.
Example:
```bash
OPENWEATHERMAP_API_KEY = 'your-api-key-here'
```
### 6.Start the development server
```bash
python manage.py runserver
```
### 7.Access the app
Open your browser and go to http://127.0.0.1:8000/

Input a city name, and it will display the current weather details.





