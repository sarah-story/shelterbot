from state_management.models import ContactState
import logging

logger = logging.getLogger(__name__)

def save_state(handler_name, msg):
    state, _ = ContactState.objects.get_or_create(connection=msg.connections[0])
    logger.debug("State is: %s" % state)
    state.handler = handler_name
    logger.debug("Saving state as %s" % state.handler)
    state.save()