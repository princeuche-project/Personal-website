answer = input('Do you want to play this game? YES/NO ').lower().strip()
if answer == 'yes':
    print(' Nice! the game is gonna be fun!')
    print()
    answer = input('''present a dragon attacking a town, where the possibility to escape is to run to a 
house bassement or stay and fight. Would you like to run to the [BASSEMENT/FIGHT] ''')
    if answer == 'bassement':
        print()
        print('If you were not able to reach in the time that was given and by the right roads you will be catch and you will lose ')
        print()
        answer = input('''The dragon is pursuing you and you have to run fast and you must find ten keys and five golds that are hidden.
when the ten keys and five golds are found, the door to escape will be open immediatly. [TEN KEYS PLUS FIVE GOLDS FOUND/NONE] ''')
        print()
        if answer == 'ten keys plus five golds found':
            print('The door to escape is open. Congratulation you win!')
        elif answer == 'none':
            print('You need those keys and gold to be save. You lose!')
            print()
        else:
            print('Invalid option you lose')
    elif answer == 'fight':
       answer = input('you stay and fight but for you to win, you must have a green light for life. [GREEN LIGHT/RED] ')
       print()
       if answer == 'green light':
        print('You are getting more strenght and more life to win and escape')
        print()
        print('Congratulations! you have won.')
       elif answer == 'red':
            print('You have no strenght and your life is limit. you cant escape')
            print()
            answer = input('Would you like to retry angain? [YES/NO] ')
            if answer == 'yes':
                print('Nice choice! this time you may be able to escape and save your life.')
                print()
                answer = input('This time, what you have to do is to pick up a gold of life and be saved. Would you like to pick the gold on the floor? [YES/NO] ')
                if answer == 'yes':
                    print()
                    print('Congratulations! you are now saved.')
                elif answer == 'no':
                    print('No other option left for you. You lose the game!')
            elif answer == 'no':
                print('It would have been a good idea for you to try it out, you may have the chance to be safe and escape')

       else:
        print('Invalid option. try again ')

else:
    answer == 'no'
    print('You would have like to try it out. Game out!')
