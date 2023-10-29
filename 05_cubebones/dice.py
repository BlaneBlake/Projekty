from random import randint

def dice(): # xDy+z
    throw = input('wzór na rzut: xDy+z\npowiedz jaki rzut wykonać:\n')
    dices = {'D3' : randint(1, 3), 'D4' : randint(1, 4),
             'D6' : randint(1, 6), 'D8' : randint(1, 8),
             'D10' : randint(1, 10), 'D12' : randint(1, 12),
             'D20' : randint(1, 20), 'D100' : randint(1, 100)}
    throw = list(throw)
    numbers_of_dices = throw[0:throw.index("D")]
    try:
        dices_type = ''.join(throw[throw.index("D"):throw.index("+")])
    except ValueError:
        dices_type = ''.join(throw[throw.index("D"):throw.index("-")])
    except ValueError:
        dices_type = ''.join(throw[throw.index("D"):])
    print(numbers_of_dices)
    print(dices_type)

    result = ''
    return result

print(dice())