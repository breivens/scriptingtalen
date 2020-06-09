from random import choice


def buzzphrase1(buzzlists):
    return " ".join([choice(buzzlist) for buzzlist in buzzlists])


def buzzphrase2(*buzzlists):
    return buzzphrase1(buzzlists)
