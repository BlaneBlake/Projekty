def what_numb_u_think():
    min = 0
    max = 1000
    answer = None

    while answer != "Y":
        guess = (max-min) // 2 + min
        print('I guess: ', guess)
        answer = input("(Y)ou win | Too (s)mall | Too (b)ig\n")

        if answer == "y":
            return f"I won. You choose {guess}"
        elif answer == "s":
            min = guess
        elif answer == "b":
            max = guess
        else:
            print('Error, try again:\n')



choose_numb = int(input("Choose a number between 1 and 1000:\n"))

print(what_numb_u_think())