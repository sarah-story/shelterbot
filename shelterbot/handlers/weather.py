import logging
import random
from rapidsms.contrib.handlers.handlers.base import BaseHandler
from ..utils import terminal_dialog


logger = logging.getLogger(__name__)


class WeatherHandler(BaseHandler):

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
                # TODO: store this user and their state
            return True

    @staticmethod
    def get_weather():
        # TODO - actually query weather
        return random.randrange(0, 40, 1) # FIXME
