from random import randint


def guess_the_number():
    rand_numb = randint(1, 100)
    answer = None
    while answer != rand_numb:
        try:
            answer = int(input("Guess the number: "))
        except ValueError:
            answer = int(input("This is not number. Try again: "))

        if answer < rand_numb:
            print("Too small")
        elif answer > rand_numb:
            print('Too big')
        else:
            return 'You win'


print(guess_the_number())
