import pytest
from unittest.mock import patch


from project import make_url, get_weather, display_forecast_choice

def test_make_url(requests_mock):
    city = "New York"
    expected_query = "http://api.openweathermap.org/data/2.5/forecast?q=New+York&units=metric&appid=4a667b3caefe6915603d5d48f02b50d7"
    requests_mock.get(expected_query, json={})
    assert make_url(city) == expected_query

def test_get_weather(requests_mock):
    city = "New York"
    expected_response = {}
    query_url = make_url(city)
    requests_mock.get(query_url, json=expected_response)
    assert get_weather(query_url) == expected_response

@patch('builtins.input', side_effect=['today'])
@patch('sys.exit')
def test_display_forecast_choice_exit_on_invalid_input(mock_exit, mock_input):
    weather_data = {
        "list": [],
        "city": {"name": "New York"}
    }
    display_forecast_choice(weather_data)
    assert mock_exit.called_with("Invalid choice. Please enter 'today' or 'tomorrow'.")

if __name__ == "__main__":
    pytest.main()
