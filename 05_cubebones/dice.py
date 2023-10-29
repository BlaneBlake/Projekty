from random import randint

def dice(): # xDy+z
    throw = input('wzór na rzut: xDy+z\npowiedz jaki rzut wykonać:\n')
    dices = {'D3' : randint(1, 3), 'D4' : randint(1, 4),
             'D6' : randint(1, 6), 'D8' : randint(1, 8),
             'D10' : randint(1, 10), 'D12' : randint(1, 12),
             'D20' : randint(1, 20), 'D100' : randint(1, 100)}
    throw = list(throw)

    if throw[0] == "D" or throw[1] == "D":
        print('Poprawna komenda')
    else:
        print("podałeś złą komendę")

    if throw[0] == "D":
        numbers_of_dices = 1
        del throw[0]
    else:
        numbers_of_dices = throw[0:throw.index("D")]
        del throw[0:throw.index("D")]

    try:
        dices_type = ''.join(throw[throw.index("D"):throw.index("+")])
        del throw[throw.index("D"):throw.index("+")]
    except ValueError:
        try:
            dices_type = ''.join(throw[throw.index("D"):throw.index("-")])
            del throw[throw.index("D"):throw.index("-")]
        except ValueError:
            dices_type = ''.join(throw[throw.index("D"): ])
            del throw[throw.index("D"): ]

    #if throw.index("+") not in throw or throw.index("-") not in throw:
    modifier = ''.join(throw)


    print(numbers_of_dices)
    print(dices_type)
    print(modifier)

    result = ''
    return result

print(dice())