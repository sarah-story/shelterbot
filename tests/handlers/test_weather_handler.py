from rapidsms.tests.harness import RapidTest
from shelterbot.handlers import weather
from shelterbot.utils import terminal_dialog
from mock import patch

class WeatherHandlerTest(RapidTest):

    @patch('shelterbot.handlers.weather.weather_util')
    def test_multiple_casing(self, weather_util):
        weather_util.get_wondergound_json.side_effect = Exception("contrived failure")
        for value in ['weather', 'Weather', 'WEATHER', 'WeaTHeR']:
            self.receive(value, self.lookup_connections('1112223333')[0])
            # this also validates us nicely handling an error state where we can't look up
            self.assertEqual(self.outbound[0].text, weather.WEATHER_LOOKUP_ERROR_RESPONSE)

    def test_wunderground_response_parse(self):
        with open("tests/resources/wunderground_response.json", "r") as f:
            self.assertEqual(31, weather.WeatherHandler.get_low_from_wondergound_json(f.read()))

    @patch('shelterbot.handlers.weather.weather_util')
    def test_cold_weather_decision(self, weather_util):

        # when cold
        cold_json = '{"forecast":{"simpleforecast":{"forecastday":[{"low":{"fahrenheit": 10}}]}}}'
        weather_util.get_wondergound_json.return_value = cold_json
        self.receive('weather', self.lookup_connections('1112223333')[0])

        # then it is seen as cold
        self.assertEqual(self.outbound[0].text, weather.TEMPERATURE_RESPONSE%10)
        # and emergency shelters are offered
        self.assertEqual(self.outbound[1].text, weather.EMERGENCY_SHELTERS_ARE_AVAILABLE)

    @patch('shelterbot.handlers.weather.weather_util')
    def test_warm_weather_decision(self, weather_util):

        # when warm
        warm_json = '{"forecast":{"simpleforecast":{"forecastday":[{"low":{"fahrenheit": 100}}]}}}'
        weather_util.get_wondergound_json.return_value = warm_json
        self.receive('weather', self.lookup_connections('2223334444')[0])

        # then it is seen as warm
        self.assertEqual(self.outbound[0].text, weather.TEMPERATURE_RESPONSE % 100)
        # and normal shelters are offered
        self.assertEqual(self.outbound[1].text, terminal_dialog.NORMAL_SHELTERS_ARE_OPEN)

