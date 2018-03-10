from rapidsms.contrib.handlers.handlers.base import BaseHandler
from state_management.models import ContactState
from shelterbot import handlers
from shelterbot.utils import send_error_message


class DefaultHandler(BaseHandler):
    @classmethod
    def dispatch(cls, router, msg):
        try:
            state = ContactState.objects.get(connection=msg.connections[0])
        except ContactState.DoesNotExist:
            return False

        try:
            handler = getattr(handlers, state.handler)
        except AttributeError:
            state.delete()
            send_error_message(msg)
            return True

        state.delete()
        return handler.dispatch(router, msg)
