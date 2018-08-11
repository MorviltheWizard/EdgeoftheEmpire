import random

setback_dice = ['Failure', 'No effect', 'Threat', 'No effect', 'Failure', 'Threat']

def roll_setback_dice():
    result = random.choice(setback_dice)
    return result

if __name__ == '__main__':
    s = roll_setback_dice()
    print("Setback: {}".format(s))
