from rapidsms.tests.harness import RapidTest
from mock import patch

class WeatherHandlerTest(RapidTest):

    def test_multiple_casing(self):
        self.receive('weather', self.lookup_connections('1112223333')[0])
        self.assertEqual(self.outbound[0].text, "I'm having trouble looking up what the weather will be tonight.")