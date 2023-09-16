# Weather App
#### Video Demo:  https://youtu.be/AhRKNYq4Q5Q
#### Description:

The Weather App is a simple command-line application that retrieves weather forecasts for a specific city. It uses the OpenWeatherMap API to retrieve the weather data and displays the forecast for today or tomorrow, including the temperature, a description of the weather and an emoji to represent the type of weather.

Please note that this app requires a valid API key from OpenWeatherMap. Get your own API key at https://openweathermap.org/.

*Features*

- **User input**: Users can enter the name of a city to retrieve the weather forecast.

- **Forecast options**: Users can view today's or tomorrow's forecast.

- **Weather visualisation**: The app displays the temperature, weather description and an emoji representing the weather type.

*Design choices*

When designing the Weather app, several design choices were considered to create an easy to use and informative experience.

- **Retry mechanism**: The application uses the retry decorator to handle potential network errors when making requests to the API. By retrying the request multiple times with a small delay, the application improves its reliability and resilience to transient network issues.

- **Colour coded temperature**: To improve the visual representation of temperature, different colours have been assigned based on temperature ranges. This provides a quick visual indication of the temperature level, making it easier for users to interpret the forecast at a glance.

- **Weather emoticons**: The inclusion of emoticons representing different weather conditions adds a touch of visual appeal to the forecast. 

- **Input validation**: The app validates the user's input to ensure that a valid city name and forecast selection have been entered. 

*Dependencies*

- Python 3.x
- requests library
- retry library
