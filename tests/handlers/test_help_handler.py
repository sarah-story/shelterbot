from rapidsms.tests.harness import RapidTest
from mock import patch

class HelpHandlerTest(RapidTest):

    @patch('shelterbot.handlers.help.settings')
    def test_base_path(self, settings):
        settings.ALLOWED_KEYWORDS = {
            'TEST KEYWORD': 'test help text'
        }
        self.receive('help', self.lookup_connections('1112223333')[0])
        self.assertEqual(
            self.outbound[0].text,
            'Allowed commands are: TEST KEYWORD. Send HELP <command> for more help on a specific command.'
        )

    @patch('shelterbot.handlers.help.settings')
    def test_base_path_with_keyword(self, settings):
        settings.ALLOWED_KEYWORDS = {
            'TEST KEYWORD': 'test help text'
        }
        self.receive('help test keyword', self.lookup_connections('1112223333')[0])
        self.assertEqual(
            self.outbound[0].text,
            'test help text'
        )

    @patch('shelterbot.handlers.help.settings')
    def test_base_path_with_invalid_keyword(self, settings):
        settings.ALLOWED_KEYWORDS = {
            'TEST KEYWORD': 'test help text'
        }
        self.receive('help something', self.lookup_connections('1112223333')[0])
        self.assertEqual(
            self.outbound[0].text,
            'Allowed commands are: TEST KEYWORD. Send HELP <command> for more help on a specific command.'
        )
