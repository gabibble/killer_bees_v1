from module1 import attack
from module1 import round as r

wrong_guess = 0
turn = 0

while turn < 3:
    print(f"\n>o< KILLER BEE GAME! ROUND {turn+1} >o<")
    print("\nOh no! This little guy is being attacked by flesh eating bees. You have 6 chances to save him!")
    print("guess the correct letters in the word/phrase or he's going down!")
    print(attack(0))
    # can't figure out why but this ends the whole game 
    # quit = input("To begin round, press go. To exit game, enter quit.")
    # if quit.lower() == quit:
    #     break
    blank_phrase = r(turn)['blank']
    while True: 
        if blank_phrase == r(turn)['answer']:
            print("\n* * * "+"".join(blank_phrase)+" * * *")
            print("\n* * * * * * * * * * * YOU WIN * * * * * * * * * * * * *\n\n")
            break
        print("\nPhrase: "+"".join(blank_phrase))
        letter = input("\nguess a letter: ").upper()
        if letter == "quit":
            break

        if letter in r(turn)['answer']:
            print("You got it!")
            for x in range(len(r(turn)['answer'])):
                if letter == r(turn)['answer'][x]:
                    blank_phrase[x] = r(turn)['answer'][x]
        else:
            wrong_guess += 1
            print(attack(wrong_guess))
            if wrong_guess == 6:
                break
    turn += 1
        
        
        