from rapidsms.contrib.handlers.handlers.base import BaseHandler
from ..utils import terminal_dialog


class WalkingDistanceDecisionHandler(BaseHandler):
    """
    For when the user has been asked if they can walk to an
    emergency shelter
    """

    @classmethod
    def dispatch(cls, router, msg):
        msg_txt = msg.text.lower()
        if msg_txt == "yes" or msg_txt == "y":
            return terminal_dialog.goodluck(msg)
        elif msg_txt == "no" or msg_txt == "n":
            # TODO: list pickup locations
            return False # FIXME