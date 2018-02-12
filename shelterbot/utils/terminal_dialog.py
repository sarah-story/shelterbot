NORMAL_SHELTERS_ARE_OPEN = "Tonight, normal shelters will be open"


def list_standard_shelters(msg):
    msg.respond("%s" % NORMAL_SHELTERS_ARE_OPEN)
    # TODO list normal shelters
    # for shelter in normal_shelters:
    #    msg.respond(shelter.print_shelter_address)
    return goodluck(msg)

def goodluck(msg):
    msg.respond("Good luck!")
    return True