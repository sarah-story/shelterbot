
import urllib2
import json

from rapidsms.contrib.handlers.handlers.base import BaseHandler
from emergency_shelter_decision import EmergencyShelterDecisionHandler
from shelterbot.utils import terminal_dialog, save_state


class WeatherHandler(BaseHandler):
    """
    For a user to ask what the weather is tonight
    """

    @classmethod
    def dispatch(cls, router, msg):
        if msg.text.lower() == "weather":
            tonight_temp = cls.get_weather()
            msg.respond("The temperature tonight should be about %d degrees" % tonight_temp)
            if tonight_temp > 25:
                terminal_dialog.list_standard_shelters(msg)
            else:
                msg.respond("Tonight, emergency shelters will be available")
                msg.respond("Would you like to go to one?")
                save_state(EmergencyShelterDecisionHandler.__name__, msg)
            return True

    @staticmethod
    def get_weather():
        # TODO - Maybe we need to structure some try/exception handling here? Not sure where to start here

        # Weather Underground API -- pulling in Nashville's Weather
        # TODO - make the city/search url dynamic for other locales
        api_call = urllib2.urlopen(
            'http://api.wunderground.com/api/69ea94c94dd51287/forecast/q/TN/Nashville.json')  # Nashville hard-coded
        json_string = api_call.read()
        parsed_json = json.loads(json_string)

        # Grab the Low Temperature from the forecast of today ([0]) and convert to integer
        low_temp = parsed_json['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit']
        low_temp = int(low_temp)

        # Close the api_call
        api_call.close()

        return low_temp

