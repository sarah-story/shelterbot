import json

from rapidsms.contrib.handlers.handlers.base import BaseHandler
from emergency_shelter_decision import EmergencyShelterDecisionHandler
from shelterbot.utils import terminal_dialog, save_state, weather_util
from shelterbot.settings import WUNDERGROUND_API_KEY, WUNDERGROUND_LOCALE
import logging
import sys
import traceback

EMERGENCY_SHELTERS_ARE_AVAILABLE = "Tonight, emergency shelters will be available"
TEMPERATURE_RESPONSE = "The temperature tonight should be about %d degrees"
WEATHER_LOOKUP_ERROR_RESPONSE = "I'm having trouble looking up what the weather will be tonight."

logger = logging.getLogger(__name__)

class WeatherHandler(BaseHandler):
    """
    For a user to ask what the weather is tonight
    """

    @classmethod
    def dispatch(cls, router, msg):
        if msg.text.lower() == "weather":
            tonight_temp = cls.get_weather()
            if tonight_temp is None:
                msg.respond(WEATHER_LOOKUP_ERROR_RESPONSE)
            else:
                msg.respond(TEMPERATURE_RESPONSE % tonight_temp)
            if tonight_temp is None or tonight_temp > 25:
                terminal_dialog.list_standard_shelters(msg)
            else:
                msg.respond(EMERGENCY_SHELTERS_ARE_AVAILABLE)
                msg.respond("Would you like to go to one?")
                save_state(EmergencyShelterDecisionHandler.__name__, msg)
            return True

    @classmethod
    def get_low_from_wondergound_json(cls, json_string):
        parsed_json = json.loads(json_string)

        # Grab the Low Temperature from the forecast of today ([0]) and convert to integer
        low_temp = \
            parsed_json['forecast']['simpleforecast']['forecastday'][0]['low'][
                'fahrenheit']
        return int(low_temp)

    @classmethod
    def get_weather(cls):
        try:
            json_string = weather_util.get_wondergound_json(WUNDERGROUND_API_KEY, WUNDERGROUND_LOCALE)
            low_temp = cls.get_low_from_wondergound_json(json_string)

            return low_temp
        except:
            logger.error("Something went wrong with getting the weather")
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value,
                                               exc_traceback)
            logger.error(''.join('!! ' + line for line in lines))
            return None
