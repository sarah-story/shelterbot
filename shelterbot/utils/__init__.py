import logging

from state_management.models import ContactState
from shelterbot import settings

logger = logging.getLogger(__name__)


def save_state(handler_name, msg):
    state, _ = ContactState.objects.get_or_create(connection=msg.connections[0])
    logger.debug("State is: %s" % state)
    state.handler = handler_name
    logger.debug("Saving state as %s" % state.handler)
    state.save()


def send_error_message(msg, available_commands=None):
    msg_txt = msg.text.lower()
    if not available_commands:
        available_commands = settings.ALLOWED_KEYWORDS.keys()
    keyword_text = ", ".join(available_commands)
    msg.respond(
        "Sorry, I didn't understand your last text: \"{}\". Can you try again? The available options are: {}"
        .format(msg_txt, keyword_text)
    )
