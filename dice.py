import random

d6 = ['one', 'two', 'three', 'four', 'five', 'six']

def roll_dice():
    result = random.choice(d6)
    return result

if __name__ == '__main__':
    dice_one = roll_dice()
    print(dice_one)
