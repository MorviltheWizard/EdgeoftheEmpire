import random

setback_dice = ['Failure', 'No effect', 'Threat', 'No effect', 'Failure', 'Threat']

def roll_setback_dice():
    result = random.choice(setback_dice)
    return result

boost_dice = ['Success', 'Advantage', 'Success, Advantage', 'Advantage, Advantage', 'No Effect', 'No Effect']
def roll_boost_dice():
    result = random.choice(boost_dice)
    return result

proficiency_dice = ['Success', 'Success', 'Success, Success', 'Advantage', 'Triumph', 'Advantage, Advantage', 'Success, Success', 'No effect', 'Advantage, Success', 'Advantage, Success', 'Advantage, Advantage', 'Advantage, Advantage' ]
def roll_proficiency_dice():
    result = random.choice(proficiency_dice)
    return result

challenge_dice = ['Threat', 'Threat', 'Threat, Threat', 'Threat, Threat', 'Failure', 'Failure', 'Failure, Failure', 'Failure, Failure', 'Despair', 'Failure, Threat', 'Failure, Threat', 'No Effect']

def roll_challenge_dice():
    result = random.choice(challenge_dice)
    return result

ability_dice = ['Success', 'Success', 'Advantage', 'Advantage', 'Advantage, Advantage', 'Success, Success', 'Advantage, Success', 'No effect']

def roll_ability_dice():
    result = random.choice(ability_dice)
    return result

difficulty_dice = ['Threat', 'Threat', 'Threat', 'Failure', 'Threat, Threat', 'Threat, Failure', 'Failure, Failure', 'No Effect']

def roll_difficulty_dice():
    result =random.choice(difficulty_dice)
    return result


def skill_check(skill, characteristic, difficulty, challenge, boost, setback):
    # ability total is largest of (skill, characterstic) minus the lowest of thise
    # proficiency total is smallest of (skill, characteristic)
    if skill > characteristic:
        ability = skill - characteristic
        proficiency = characteristic
    else:
        ability = characteristic - skill
        proficiency = skill
    for i in range(0, ability):
        print("Ability: {}".format(roll_ability_dice()))
    for i in range(0, proficiency):
        print("Proficiency: {}".format(roll_proficiency_dice()))
    


if __name__ == '__main__':
    skill_check(3, 2, 2, 0, 1, 1)
    # s = roll_setback_dice()
    # b = roll_boost_dice()
    # p = roll_proficiency_dice()
    # c = roll_challenge_dice()
    # a = roll_ability_dice()
    # d = roll_difficulty_dice()
    # print("Setback: {}".format(s))
    # print("Boost: {}".format(b))
    # print("Proficiency: {}".format(p))
    # print("Challenge: {}".format(c))
    # print("Ability: {}".format(a))
    # print("Difficulty: {}".format(d))
