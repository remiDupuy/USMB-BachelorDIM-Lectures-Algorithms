# coding: utf-8

import random

score_user = 0
score_computer = 0


USER_TURN = 1
COMPUTER_TURN = 2


current_player = USER_TURN
## Execute each turn until one score is > 100
while score_computer < 100 and score_user < 100:

    if(current_player == USER_TURN) :
        print('\n\nUSER TURN')

        exit = 0
        current_player = COMPUTER_TURN


        turn_score = 0
        while(not exit) :
            dice_value = random.randint(1, 6)
            print 'Valeur lancé de dé : {dice_value}'.format(dice_value=dice_value)

            if(dice_value == 1):
                print 'Vous avez perdu le tour'
                print 'Votre score est de {score}'.format(score=score_user)
                exit = 1
                continue

            turn_score += dice_value
            print 'Le score de votre tour est de {score}'.format(score=turn_score)
            wantsToExit = input('Voulez vous continuer ? (0 = Oui/1 = non)')
            if(wantsToExit) :
                score_user += turn_score
                print 'Votre score est de {score}'.format(score=score_user)
                exit = 1
                continue

    if (current_player == COMPUTER_TURN):
        print('\n\nCOMPUTER TURN')

        exit = 0
        current_player = USER_TURN

        turn_score = 0
        while (not exit):
            dice_value = random.randint(1, 6)
            print 'Lancé de dé ordinateur : {dice_value}'.format(dice_value=dice_value)

            if (dice_value == 1):
                print 'Vous avez perdu le tour'
                print 'Score ordinateur est de {score}'.format(score=score_computer)
                exit = 1
                continue

            turn_score += dice_value
            print 'Le score du tour ordinateur est de {score}'.format(score=turn_score)
            wantsToExit = random.randint(0,1)
            if (wantsToExit):
                score_computer += turn_score
                print 'Score ordinateur est de {score}'.format(score=score_computer)
                exit = 1
                continue

            raw_input('Pause....')

if(score_computer > 100):
    print 'ORDINATEUR GAGNANT !!!!'
else :
    print 'USER GAGNANT !!!!'







