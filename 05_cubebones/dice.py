from random import randint

def dice(): # xDy+z
    throw = input('wzór na rzut: xDy+z\npowiedz jaki rzut wykonać:\n')
    # dices = {'D3' : randint(1, 3), 'D4' : randint(1, 4),
    #          'D6' : randint(1, 6), 'D8' : randint(1, 8),
    #          'D10' : randint(1, 10), 'D12' : randint(1, 12),
    #          'D20' : randint(1, 20), 'D100' : randint(1, 100)}
    dices = ['D3', 'D4',
             'D6', 'D8',
             'D10', 'D12',
             'D20', 'D100']


    # MORE COMPLICATED COMMAND TEST
    test_command = False
    for i in dices:
        if i in throw:
            test_command = True

    if test_command == True:
        print("Poprawna komenda")

        throw = list(throw)

        if throw[0] == "D":
            numbers_of_dices = 1
        else:
            numbers_of_dices = ''.join(throw[0:throw.index("D")])
            del throw[0:throw.index("D")]
        print(throw)
        try:
            dices_type = ''.join(throw[throw.index("D"):throw.index("+")])
            del throw[throw.index("D"):throw.index("+")]
        except ValueError:
            try:
                dices_type = ''.join(throw[throw.index("D"):throw.index("-")])
                del throw[throw.index("D"):throw.index("-")]
            except ValueError:
                dices_type = ''.join(throw[throw.index("D"):])
                del throw[throw.index("D"):]
        print(throw)

        if throw == []:
            modifier = 0
        elif throw[0] == "+":
            modifier = int(''.join(throw[1:]))
        elif throw[0] == "-":
            modifier = int(''.join(throw))

        print()
        print(numbers_of_dices)
        print(dices_type)
        print(modifier)
        print()

        result = 0
        #!!!!! nie losuje liczby oczek
        #losuje raz zmienną w słowniku i przypisuje ją do zmiennej
        # for i in range(int(numbers_of_dices)):
        #     print(dices[f'{dices_type}'])
        #     result += dices[dices_type]
        #     # print(result)
        # result += modifier
        for i in range(int(numbers_of_dices)):
            t = int(dices_type.split('D')[1])
            result += randint(1, t)
        result += modifier
    else:
        result = 'Błędna komenda'




    return 'Wynik rzutu: ' + str(result)

print(dice())