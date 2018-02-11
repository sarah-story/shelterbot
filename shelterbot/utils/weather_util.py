import urllib2

def get_wondergound_json(api_key, locale):
    # Weather Underground API -- pulling in Weather
    api_call = urllib2.urlopen(
        'http://api.wunderground.com/api/' + api_key + '/forecast/q/' + locale + '.json')
    response = api_call.read()

    # Close the api_call
    api_call.close()

    return response
