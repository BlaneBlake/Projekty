from random import randint


def lotto_draw():
    win_numbers = []
    while len(win_numbers) < 6:
        num = randint(1, 49)
        if num not in win_numbers:
            win_numbers.append(num)
    win_numbers.sort()
    return win_numbers

def lotto_type():
    type_numbers = []
    while len(type_numbers) < 6:
        try:
            num = int(input('enter a number between 1 and 49:\n'))
            if num not in type_numbers and num >= 1 and num <= 49:
                type_numbers.append(num)
            else:
                print('You selected this number earlier, or you entered a number outside the range, please try again.\n')
        except ValueError:
            print("\n !!! This is not number. !!!\n")
    type_numbers.sort()
    return type_numbers

def lotto_results(lotto_num, your_types):
    good_nums = 0
    for i in your_types:
        good_nums += lotto_num.count(i)
    return f'you got it {good_nums} times'

types = lotto_type()
rand_nums = lotto_draw()

print('you choose: ', types)
print('results: ', rand_nums)
print(lotto_results(rand_nums, types))

