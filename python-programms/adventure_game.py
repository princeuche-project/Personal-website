from multiprocessing.connection import answer_challenge


print('Welcome to the most adventure game. Please kindly follow the instructions to play!')
print()
answer = input("You are walking on the street, and you saw a two deadly animal standing in front of you. What would you do? [RUN/FIGHT] ").lower().strip()
if answer == 'run':
    print()
    answer = input('You have two ways out. the direction that lead to the crowd and the lonly area. are you going to run to the [CROWD/LONLY AREA]? ')
    print()
    if answer == 'crowd':
       print('You made the wrong choice because the animal is going to harm the people around that area. Game over!')
       print()
    elif answer == 'lonly area':
        answer = input('You have made the right decision by following the lonly area. and now for you to be safe, you need to call for help. Would you like to call the [POLICE/YOUR BROTHER?] ')
        print()
    if answer == 'police':
            print('Right choice! the police are comming to help you out. keep on going..')
    elif answer == 'your brother':
        print('wrong choice because your brother can not help you at the moment.')
else:
   answer == 'fight'
   print()
   print('Hop! this is a very dangerous decision. you cant fight a deadly animal. you need to reconsider your choice.')
   print('Game Over!')

# answer = input('You are on your way to the city mall, you saw an injured person lying down on the floor. What would you do [HELP/IGNORE?] ').lower().strip()
# if answer == 'help':

#     answer = input('In order for you to be of help, What would you do? [INFORM_THE_POLICE / INFORM THE AMBLANCE?] ').lower().strip()
#     if answer == 'inform the amblance':
#         answer == input('what number would you use to call the amblance [911/998] ') 
#         if answer == '998':
#             print('you have contributed in savinf a soul! good job.') 
#         else:
#            answer == '911'
#         print('You have tired but the first to call is the amblance before the police.') 
#     elif answer == 'inform the police':
#         answer = input('What number would you use to call the police? [998/911] ')
#     if answer == '998':
#       print('you have made the right choice.')
# else:
#     print('---')