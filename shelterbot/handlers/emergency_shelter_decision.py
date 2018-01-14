from rapidsms.contrib.handlers.handlers.base import BaseHandler
from walking_distance_decision import WalkingDistanceDecisionHandler
from shelterbot.utils import terminal_dialog, save_state


class EmergencyShelterDecisionHandler(BaseHandler):
    """
    For when the user has been asked if they would like to go to an
    emergency shelter
    """

    @classmethod
    def dispatch(cls, router, msg):
        msg_txt = msg.text.lower()
        if msg_txt == "yes" or msg_txt == "y":
            msg.respond("Great! These are your options:")
            # TODO: print all the emergency shelters
            msg.respond("Can you get to any of those on your own?")
            save_state(WalkingDistanceDecisionHandler.__name__, msg)
            return True
        elif msg_txt == "no" or msg_txt == "n":
            return terminal_dialog.list_standard_shelters(msg)