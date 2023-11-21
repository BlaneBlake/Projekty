from flask import Flask, request, render_template
from random import randint, choice
app = Flask(__name__)

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
        return 'Wrong dices. Try again' + render_template("choose_dices.html")


def sum_points(player_points, throw_points):
    if throw_points == 7:
        return player_points // 7
    elif throw_points == 11:
        return player_points * 11
    else:
        return player_points + throw_points


@app.route("/2001", methods=['GET', 'POST'])
def form():
    if request.method == "GET":
       return render_template("choose_dices.html", first_throw='True', human_player=0, computer_player=0, human_throw=0, computer_throw=0)
    else:
    #jesli kostki w html nie mają ustawionego atrybutu checked to brak wybranej kości wywołuje KeyError
        first_dice = request.form["dice_1"]
        second_dice = request.form["dice_2"]
        first_throw = request.form["first_throw"]

        if first_throw == 'True':
            human_throw = dices_throw(first_dice, second_dice)
            computer_throw = dices_throw()
            human_player = human_throw
            computer_player = computer_throw
            first_throw = 'False'
            return 'pierwszy rzut' + render_template("points.html", human_player=human_player, computer_player=computer_player, \
                                                     human_throw=human_throw, computer_throw=computer_throw) + \
                render_template("choose_dices.html", first_throw=first_throw, human_player=human_player, \
                                computer_player=computer_player, human_throw=human_throw, computer_throw=computer_throw)
        else:

            human_player = int(request.form["human_player"])
            computer_player = int(request.form["computer_player"])
            print('test',human_player, computer_player)


            while human_player < 2001 and computer_player < 2001:
                human_throw = dices_throw(first_dice, second_dice)
                computer_throw = dices_throw()
                human_player = sum_points(human_player, human_throw)
                computer_player = sum_points(computer_player, computer_throw)
                print('test1', human_player, computer_player)

                if human_player >= 2001:
                    return f'you won {human_player}, {human_throw}'

                elif computer_player >= 2001:
                    return f'Computer won {computer_player}, {computer_throw}'
                return 'gra' + render_template("points.html", human_player=human_player, computer_player=computer_player, \
                                           human_throw=human_throw, computer_throw=computer_throw) + \
                render_template("choose_dices.html", first_throw=first_throw, human_player=human_player, computer_player=computer_player, \
                                human_throw=human_throw, computer_throw=computer_throw)


app.run(debug=True)

