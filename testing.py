
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

   force_sensitivity = [
        'Yes: This costs 20 XP',
        'No',
    ]
    

    def choose_force_sensitivity(self):
        self.force_sensitivity = choose("Are you force sensitive?", self.force_sensitivity)
        print("Chosen {}".format(self.force_sensitivity))
        if self.force_sensitivity = 'Yes: This costs 20 XP'
            self.choose_force_sensitivity = -20 starting experience 
             

