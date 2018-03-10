from shelters.models import Shelter
NORMAL_SHELTERS_ARE_OPEN = "Tonight, these normal shelters will be open: \n"


def list_standard_shelters(msg):
    response = NORMAL_SHELTERS_ARE_OPEN
    i = 1
    for shelter in Shelter.objects.iterator():
        response += str(i) + ") " + str(shelter) + "\n"
        i += 1
    msg.respond(response)
    return goodluck(msg)


def goodluck(msg):
    msg.respond("Good luck!")
    return True
