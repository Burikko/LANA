import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        parameters = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url, params=parameters)
        return response.json()

# Example usage
# weather_api = WeatherAPI('YOUR_API_KEY')
# print(weather_api.get_weather('London'))