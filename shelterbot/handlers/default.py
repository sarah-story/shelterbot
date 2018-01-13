from rapidsms.contrib.handlers.handlers.base import BaseHandler
from state_management.models import ContactState
from shelterbot import handlers


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
            return False

        state.delete()
        return handler.dispatch(router, msg)
