from random import randint

def dices_throw():
    return randint(1, 6) + randint(1, 6)

def sum_points(player_points, throw_points):
    if throw_points == 7:
        return player_points // 7
    elif throw_points == 11:
        return player_points * 11
    else:
        return player_points + throw_points

input('press enter to throw dices.\n')
human_player = dices_throw()
print('You have', human_player, ' points.')
computer_player = dices_throw()
print('Computer have', computer_player, 'points.')

while human_player < 2001 and computer_player < 2001:
    input('\npress enter to throw dices.\n')
    human_player = sum_points(human_player, dices_throw())
    print('You have', human_player, ' points.')
    computer_player = sum_points(computer_player, dices_throw())
    print('Computer have', computer_player, 'points.')

    if human_player >= 2001:
        print('you won')

    elif computer_player >= 2001:
        print('Computer won')
