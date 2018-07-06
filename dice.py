#!/usr/local/bin/python3
import random

def roll(num,face,mod):
    """Returns random dice rolls."""

    res = 0

    if face < 2:
        raise ValueError("Die has less than 2 faces.")
    else:
        roll = [random.randint(1,face)+mod for i in range(num)]
    
    print("done")
    for i in range(len(roll)):
        res += roll[i]

    return int(res)

def crit_message(res):
    """Returns critical hit and miss messages."""

    with open("crits.txt") as messages:
        msg = [line.strip("\n") for line in messages]

    print("Selecting a random message!")
    print(random.choice(msg))

crit_message(1)
