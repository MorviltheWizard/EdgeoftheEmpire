
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

    races = {
        'Droid': {
            'Brawn': 1, 'Agility': 1, 'Cunning': 1, 'Willpower': 1, 'Presence': 1,
            'Starting Experience': 175
        },
        'Bothan': {
            'Brawn': 1, 'Agility': 2, 'Intellect': 2, 'Cunning': 3, 'Willpower': 2, 'Presence': 2,
            'Starting Experience': 100
        },
        'Gand': {
            'Brawn': 2, 'Agility': 2, 'Intellect': 2, 'Cunning': 2, 'Willpower': 3, 'Presence': 1,
            'Starting Experience': 100
        },
        'Human': {
            'Brawn': 2, 'Agility': 2, 'Intellect': 2, 'Cunning': 2, 'Willpower': 2, 'Presence': 2,
            'Starting Experience': 110
        },
        'Rodian': {
            'Brawn': 2, 'Agility': 3, 'Intellect': 2, 'Cunning': 2, 'Willpower': 1, 'Presence': 2,
            'Starting Experience': '100'
        },
        'Trandoshan': {
            'Brawn': 3, 'Agility': 1, 'Intellect': 2, 'Cunning': 2, 'Willpower': 2, 'Presence': 2,
            'Starting Experience': '90'
        },
        "Twi'lek": {
            'Brawn': 1, 'Agility': 2, 'Intellect': 2, 'Cunning': 2, 'Willpower': 2, 'Presence': 2,
            'Starting experience': '100'
        },
        'Wookie': {
            'Brawn': 3, 'Agility': 2, 'Intellect': 2, 'Cunning': 2, 'Willpower': 1, 'Presence': 2,
            'Starting experience': 90
        },
    }

    def __init__(self, name):
        self.name = name

    def choose_class(self):
        self.class_ = choose("Which class would you like?", self.classes)
        print("Chosen {}".format(self.class_))

    def class_name(self):
        return self.classes[self.class_]


    def choose_race(self):
        self.race = choose ("What race are you?", list(self.races.keys()))
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

    obligations = {
     'Addiction' = {
         'This character has a strong addiction that he must keep feeding. While it could be a physical addiction, such as spice, alcohol or stims, it coculd also be a mental addiction such as gambling or law breaking. The character devotes a lot of the time to sating this addiction. Avoiding this obligation will begin with withdrawal. Every tiem withdrawal happens, you must roll difficulty dice',
     }
    'Betrayal' = {
         'This obligation can work in one of two ways: either the character is the target of a deep and personal betrayal, or the chracter is the one who betrayed others. It could be as simple as a broken promise, or something serious like treason or mutiny. The target may seek answers, compensation or revenge.',
    }
    
     'Blackmail' = {
         "Someone has discovered this PC's dirty secrets and using tht knowledge to their own gain. To make matters worse, the blackmailer has something that could be leaked. A holovid, bank records of a weapon used during a crime, and so on and so forth. The PC must do as he's told by the blackmailer, or have their little dirty secrets leaked to the holonet, or worse, the Empire.",
     }
     'Bounty' = {
         'For some reason, this character has a price on his head. This may be a legel warrant, or a contract by a crime syndicate, collection agencies or just somebody who has had his honour attacked by the character. His background is how he earned his mark, and the character must always lay low in population centres.',
     } 
     'Criminal' = {
         'This character has a criminal record, or was accused of a crime he may not have committed. All Force Sensitive characters fall under this banner, as the Empire seeks out those who could potentially become Jedi and turn them to the Dark Side. This obligation may be settled by burying evidence, or efforts to prove his innocence',
     } 
     'Debt' = {
         'This character owes somebody a great deal of credits or something else. Maybe he has a huge gambling debt to a hutt, or is indebted to the Czerka corporation for his starship. To make matters worse, depending on who owns the debt. Even fully paying it off may not settle the score, as someone who can get that money can surely get more.',
     }
     'Dutybound' = {
         'This PC has a deep sense of the duty that he feels compelled to fulfill, such as military service or making good on a contract or maybe just some thieves code. Unlike the oath obligation (see below) this character has a legel or ritualistic obligation to an organisation which could be difficult or detrimental should they not fulfill.',
     } 
     'Family' =  {
         'This character has a deep ties with his family that requires a lot of time and attention. Whether you are an Alderaanian Noble or a descendant of Onderon Royalty, this requires a lot of time working for the family, spending time with them or simply mediating squabbling family members.',
     }
     'Favor' = {
         'This PC owes a big favour to somebody. Whether it be an Imperial Officer, who looked the other way to smuggled goods, or got him out of prison. If this obligation is selected, the one they owe a favour too could come knocking any time.',
     }
     'Oath' = {
         'This character has sworn an oath that dictates their thoughts and actions. Whether it is too a God, or a way of living such as the Jedi Code. Whatever the case the oath should be serious and hinder the PC in his journey somehow. To not fulfill this oath will cause major internal and moral struggle.',
     }
     'Obsession' = {
         'The PC has a rather unhealthy obsession he needs to fulfill. Whether it be to a region, a celebrity or some political icon, this character is often looked at with pity or amusement.',
     } 
     'Responsibility' = {
         'This character feels repsonsible for something. Where it be caring for Alderaanian children who survived their planets brutal destruction, or a strong connection to a mentor, this character must always act out their responsibility in game.',
     }
    }


    def choose_obligation(self):
        self.obligation = choose ("What is your obligation?", self.obligations)
        print("Chosen {}".format(self.obligation))

    def invest_experience(self):
        if self.specialisation == "Assassin":
            self.invest_experience = choose('Where do you place your experience?', [
             'Grit', 'Lethal Blows', 'Stalker', 'Dodge',
            ])
            
        
        if self.specialisation == "Gadgeteer":
            self.invest_experience = choose('Where do you place your experience?', [
                  'Brace', 'Toughened', 'Intimidating', 'Defensive stance',
            ])
            
            
        if self.specialisation == "Survivalist":
            self.invest_experience = choose [
                'Forager', 'Stalker', 'Outdoorsman', 'Expert Tracker',
            ]
        if self.specialisation == "Doctor":
            self.invest_experience = choose [
                'Surgeon', 'Bacta Specialist', 'Grit', 'Resolve',
            ]
        if self.specialisation == "Politico":
            self.invest_experience = choose [
                'Kill with Kindness', 'Grit', 'Plausible Deniability', 'Toughened',
            ]
        if self.specialisation == "Scholar":
            self.invest_experience = choose [
                'Respected Scholar', 'Speaks Binary', 'Grit', 'Brace',
            ]
        if self.specialisation == "Fringer":
            self.invest_experience = choose [
                'Galaxy Mapper', 'Street Smarts', 'Rapid Recovery', 'Street Smarts'
            ]
        if self.specialisation == "Scout":
            self.invest_experience = choose [
                "Rapid Recovery", 'Stalker', 'Grit', 'Shortcut',
            ]
        if self.specialisation == "Trader":
            self.invest_experience = choose [
                'Know Somebody' 'Convincing Demeanor', 'Wheel and Deal', 'Smooth talker',
            ]
        if self.specialisation == "Bodyguard":
            self.invest_experience = choose [
                'Toughened', 'Barrage', 'Durable', 'Grit',
            ]
        if self.specialisation == "Marauder":
            self.invest_experience = choose [
                'Toughened', 'Frenzied Attack', 'Feral Strength', 'Lethal Blows',
            ]
        if self.specialisation == "Mercenary":
            self.invest_experience = choose [
                'Command', 'Second Wind', 'Point Blank', 'Side Step',
            ]
        if self.specialisation == "Pilot":
            self.invest_experience = choose [
                'Full Throttle', 'Skilled Jockey', 'Galaxy Mapper', 'Lets ride', 
            ]    
        if self.specialisation == "Scoundrel":
            self.invest_experience = choose [
                'Black Market Contacts', 'Convincing Demeanor', 'Quick Draw', 'Rapid Reaction'
            ]
        if self.specialisation == "Thief":
            self.invest_experience = choose [
                'Street Smarts', 'Black Market Contacts', 'Indistingishable', 'Bypass Security',
            ]
        if self.specialisation == "Mechanic":
            self.invest_experience = choose [
                'Gearhead', 'Toughened', 'Fine Tuning', 'Solid Repairs',
            ]
        if self.specialisation == "Outlaw Tech":
            self.invest_experience = choose [
                'Tinkerer', 'Utinni!', 'Speaks Binary', 'Tinkerer',
            ]
        if self.specialisation == "Slicer":
            self.invest_experience = choose [
                'Codebreaker', 'Grit', 'Technical Aptitude', 'Bypass Security',
            ]
        if self.specialisation == "Force Sensitive Exile":
            self.invest_experience = choose [
                'Uncanny Senses', 'Insight', 'Forager', 'Uncanny Reactions',
            ]

    motivations = [
         'Ambition',
         'Cause',    
         'Relationship',
         ]

    def choose_motivation(self):
         self.motivation = choose("What is your motivation?", self.motivations)
         print ("Chosen {}".format(self.motivation)) 





    def print(self):
        print("*" * 80)
        print("* Name: {}".format(self.name))
        print("* Race: {}".format(self.race))
        print("* Class: {}".format(self.class_))
        print("* Specialisation: {}".format(self.specialisation))
        print("* obligation: {}".format(self.obligation))
        print("* First skill: {}".format(self.invest_experience))
        print("*Motivation: {}".format(self.motivation))
        print("*" * 80)



if __name__ == '__main__':
    print("What is your character's name?")
    print("> ", end="")
    name = input()
    sheet = Sheet(name)
    sheet.choose_class()
    sheet.choose_race()
    sheet.choose_specialisation()
    sheet.choose_obligation()
    sheet.invest_experience()
    sheet.choose_motivation()
    sheet.invest_experience()
    
    sheet.strength = random.randint(1,6)
    sheet.print()
