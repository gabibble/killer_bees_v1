def attack(x):
    attack = ['\n O    >o<\n/|\  >o<\n/ \    >o<\n',
            '\n O    >o<\n/|   >o<\n/ \    >o<\nOh no! he lost an arm!!',
            '\n O    >o<\n/|   >o<\n  \    >o<\nOuch! He lost an leg!',
            '\n O    >o<\n |   >o<\n  \    >o<\nWhelp, there go his arms! 3 more guesses',
            '\n O    >o<\n |   >o<\n       >o<\nOh shucks! No more limbs! 2 more guesses.',
            "\n      >o<\n |   >o<\n       >o<\nYikes! He's just a torso! You have 1 chance left.",
            '\n\n\n\n\n\n\n  >o<   >o<  >o<     >o<   >o<\n  >o< >o<   GAME OVER >o<  >o<\n    >o<   >o<  >o<   >o<\n\n\n\n\n']
    return attack[x]


def round(x):
        phrases = [
                {'blank':['_ ','_ '], 'answer':['H','I']},
                {'blank':['_ ','_ ','_ ','_ ','_ ','   ','_ ','_ ','_ ','_ ','_ '], 'answer':['H','E','L','L','O','   ','W','O','R','L','D']},
                {'blank':['_ ','   ','_ ','_ ','_ ','_ ','   ','_ ','_ ','_ ','_ ','_ ','_ '], 'answer':['I','   ','L','O','V','E','   ','P','Y','T','H','O','N']},
                # {'blank':['_ ','_ '], 'answer':['H','I']},
                # {'blank':['_ ','_ '], 'answer':['H','I']},
                # {'blank':['_ ','_ '], 'answer':['H','I']},
                # {'blank':['_ ','_ '], 'answer':['H','I']},
        ]
        return phrases[x]