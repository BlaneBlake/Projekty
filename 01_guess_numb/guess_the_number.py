from random import randint



try:
    answer = int(input("Guess the number: "))
except:
    answer = int(input("This is not number. Try again: "))