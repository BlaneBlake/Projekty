from random import randint

def dices_throw(first_dice = 'random', second_dice = 'random'):
    dices = {'D3': randint(1, 3), 'D4': randint(1, 4),
             'D6': randint(1, 6), 'D8': randint(1, 8),
             'D10': randint(1, 10), 'D12': randint(1, 12),
             'D20': randint(1, 20), 'D100': randint(1, 100)}
    if first_dice in dices and second_dice in dices:
        return dices[first_dice] + dices[second_dice]
    elif first_dice == 'random' or second_dice == 'random':
        pass
    else:
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
input('press enter to throw dices.\n')
human_player = dices_throw(first_dice, second_dice)
print('You have', human_player, ' points.')
computer_player = dices_throw(first_dice, second_dice)
print('Computer have', computer_player, 'points.')

while human_player < 2001 and computer_player < 2001:
    first_dice = input('Choose first dice ("D3, D4, D6, D8, D10, D12, D20, D100")\n')
    second_dice = input('Choose second dice ("D3, D4, D6, D8, D10, D12, D20, D100")\n')
    input('\npress enter to throw dices.\n')
    human_player = sum_points(human_player, dices_throw(first_dice, second_dice))
    print('You have', human_player, ' points.')
    computer_player = sum_points(computer_player, dices_throw(first_dice, second_dice))
    print('Computer have', computer_player, 'points.')

    if human_player >= 2001:
        print('you won')

    elif computer_player >= 2001:
        print('Computer won')
