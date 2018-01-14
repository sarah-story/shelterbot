
def list_standard_shelters(msg):
    msg.respond("Tonight, normal shelters will be open")
    # TODO list normal shelters
    # for shelter in normal_shelters:
    #    msg.respond(shelter.print_shelter_address)
    return goodluck(msg)

def goodluck(msg):
    msg.respond("Good luck!")
    # TODO: clear this user's state
    return True