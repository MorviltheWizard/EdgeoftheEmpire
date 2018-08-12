
import random


def choose(question, options):
    print(question)
    for i, opt in enumerate(options):
        print("{}) {}".format(i, opt))
    chosen = None
    while chosen == None:
        print("> ", end="")
        x = input()
        try:
            chosen = int(x)
        except ValueError:
            pass
    return chosen

class Sheet:

    classes = [
        'Bounty Hunter',
        'Colonist',
        'Explorer',
        'Hired Gun',
        'Smuggler',
        'Technician',
        'Force Sensitive Exile',
    ]
    
    def __init__(self, name):
        self.name = name

    def choose_class(self):
        self.class_ = choose("Which class would you like?", self.classes)
        print("Chosen {}".format(self.classes[self.class_]))

    def class_name(self):
        return self.classes[self.class_]

    races = [
        'Bothan',
        'Droid',
        'Gand',
        'Human',
        "Twi'lek",
        'Rodian',
        'Trandoshan',
        'Wookie',
    ]

    def choose_race(self):
        self.race = choose ("What race are you?", self.races)
        print("Chosen {}".format(self.races[self.race_]))
    

    def print(self):
        print("*" * 80)
        print("* Name: {}".format(self.name))
        print("* Class: {}".format(self.class_name()))
        print("*" * 80)

if __name__ == '__main__':
    print("What is your character's name?")
    print("> ", end="")
    name = input()
    sheet = Sheet(name)
    sheet.choose_class()
    
    sheet.strength = random.randint(1,6)
    sheet.print()
