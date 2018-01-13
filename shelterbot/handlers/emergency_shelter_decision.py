import logging
from rapidsms.contrib.handlers.handlers.base import BaseHandler
from ..utils import terminal_dialog


logger = logging.getLogger(__name__)


class EmergencyShelterDecisionHandler(BaseHandler):

    @classmethod
    def dispatch(cls, router, msg):
        msg_txt = msg.text.lower()
        if msg_txt == "yes" or msg_txt == "y":
            msg.respond("Great! These are your options:")
            # TODO: print all the emergency shelters
            msg.respond("Can you get to any of those on your own?")
            # TODO: save current state
        elif msg_txt == "no" or msg_txt == "n":
            terminal_dialog.list_standard_shelters(msg)