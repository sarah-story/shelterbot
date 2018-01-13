from rapidsms.contrib.handlers import KeywordHandler
from shelterbot import settings


class HelpHandler(KeywordHandler):
    keyword = "help"

    def help(self):
        """Invoked if someone just sends `HELP`.  We also call this
        from `handle` if we don't recognize the arguments to HELP.
        """
        keyword_text = ", ".join(settings.ALLOWED_KEYWORDS.keys())
        self.respond(
            "Allowed commands are: %s. Send HELP <command> for more help on a specific command." % keyword_text
        )

    def handle(self, text):
        text = text.strip().upper()
        message = settings.ALLOWED_KEYWORDS.get(text)
        if message:
            self.respond(message)
        else:
            self.help()
