
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
    return options[chosen]

class Sheet:

    classes = [
        'Bounty Hunter',
        'Colonist',
        'Explorer',
        'Hired Gun',
        'Smuggler',
        'Technician',
    ]
    
    def __init__(self, name):
        self.name = name

    def choose_class(self):
        self.class_ = choose("Which class would you like?", self.classes)
        print("Chosen {}".format(self.class_))

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
        print("Chosen {}".format(self.race))

    def choose_specialisation(self):
        if self.class_ == "Bounty Hunter":
            self.specialisation = choose("What specialisation of Bounty Hunter?", [
                'Assassin', 'Gadgeteer', 'Survivalist', 'Force Sensitive Exile',
            ])   
        if self.class_ == "Colonist":
            self.specialisation = choose('What specialisation of Colonist?', [
                'Doctor', 'Politico', 'Scholar', 'Force Sensitive Exile',
            ])
        if self.class_ == "Explorer":
            self.specialisation = choose('What specialisation of Explorer?', [
                'Fringer', 'Scout', 'Trader', 'Force Sensitive Exile',
            ])
        if self.class_ == "Hired Gun":
            self. specialisation = choose('What specialisation of Hired Gun?', [
                'Bodyguard', 'Marauder', 'Mercenary soldier', 'Force Sensitive Exile',
            ])
        if self.class_ == "Smuggler":
            self.specialisation = choose('What specialisation of Smuggler?', [
                'Scoundrel', 'Pilot', 'Thief', 'Force Sensitive Exile',
            ])
        if self.class_ == "Technician":
            self.specialisation = choose('What specialisation of Technician', [
                'Mechanic', 'Outlaw Tech', 'Slicer', 'Force Sensitive Exile',
            ])
         
    def print(self):
        print("*" * 80)
        print("* Name: {}".format(self.name))
        print("* Race: {}".format(self.race))
        print("* Class: {}".format(self.class_))
        print("* Specialisation: {}".format(self.specialisation))
        print("*" * 80)

if __name__ == '__main__':
    print("What is your character's name?")
    print("> ", end="")
    name = input()
    sheet = Sheet(name)
    sheet.choose_class()
    sheet.choose_race()
    sheet.choose_specialisation()
    
    sheet.strength = random.randint(1,6)
    sheet.print()
