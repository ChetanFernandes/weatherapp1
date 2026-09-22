# WeatherApp1

A small Flask web application that fetches weather data from the OpenWeatherMap API and displays it.

## Short description

WeatherApp1 is a lightweight Flask application that allows users to enter a city name and view current weather information using the OpenWeatherMap API.

## How to run

1. Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
2. Install dependencies:
   pip install -r requirements.txt
3. Set your OpenWeatherMap API key as an environment variable (optional):
   export OPENWEATHER_API_KEY=your_api_key  # Windows: set OPENWEATHER_API_KEY=your_api_key
4. Run the application:
   python app.py
5. Open http://localhost:5000 in your browser and use the form to fetch weather data.

## Dependencies

- Flask
- requests
- gunicorn (optional for production)

## Contact / Maintainer

Maintained by Chetan Fernandes. For issues and PRs, please open them on the repository: https://github.com/ChetanFernandes/weatherapp1
