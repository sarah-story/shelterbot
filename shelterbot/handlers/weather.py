import random
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
        # TODO - actually query weather
        return random.randrange(0, 40, 1) # FIXME
