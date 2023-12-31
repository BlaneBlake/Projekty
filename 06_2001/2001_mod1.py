from random import randint, choice


def dices_throw(first_dice = '', second_dice = ''):
    dices = ['D3', 'D4',
             'D6', 'D8',
             'D10', 'D12',
             'D20', 'D100']


    if first_dice == '' or second_dice == '':
        return  randint(1, int(choice(dices).split('D')[1])) + randint(1, int(choice(dices).split('D')[1]))
    elif first_dice in dices and second_dice in dices:
        return randint(1, int(first_dice.split('D')[1])) + randint(1, int(second_dice.split('D')[1]))
    else:
        # If command is wrong else is not stable !!!
        print('Wrong dices. Try again')
        first_dice = input('Choose first dice ("D3, D4, D6, D8, D10, D12, D20, D100")\n')
        second_dice = input('Choose second dice ("D3, D4, D6, D8, D10, D12, D20, D100")\n')
        return dices_throw(first_dice, second_dice)


def sum_points(player_points, throw_points):
    if throw_points == 7:
        return player_points // 7
    elif throw_points == 11:
        return player_points * 11
    else:
        return player_points + throw_points

first_dice = input('Choose first dice ("D3, D4, D6, D8, D10, D12, D20, D100")\n')
second_dice = input('Choose second dice ("D3, D4, D6, D8, D10, D12, D20, D100")\n')

human_player = dices_throw(first_dice, second_dice)
print('You have', human_player, ' points.')
computer_player = dices_throw()
print('Computer have', computer_player, 'points.')

while human_player < 2001 and computer_player < 2001:
    first_dice = input('Choose first dice ("D3, D4, D6, D8, D10, D12, D20, D100")\n')
    second_dice = input('Choose second dice ("D3, D4, D6, D8, D10, D12, D20, D100")\n')

    human_player = sum_points(human_player, dices_throw(first_dice, second_dice))
    print('You have', human_player, ' points.')
    computer_player = sum_points(computer_player, dices_throw())
    print('Computer have', computer_player, 'points.')

    if human_player >= 2001:
        print('you won')

    elif computer_player >= 2001:
        print('Computer won')
