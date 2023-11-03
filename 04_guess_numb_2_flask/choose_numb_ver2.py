from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/guess", methods=['GET', 'POST'])
def form():

    min = 0
    max = 1000
    answer = "None"

    form = request.form

    while answer != "You win":

        guess = (max-min) // 2 + min


        # min = form["min"]
        # max = form["max"]
        # answer = form["answer"]

        if answer == "You win":
            return render_template("win.html", guess=guess)
        elif answer == "Too small":
            min = guess
        elif answer == "too big":
            max = guess
        else:
            print('Error, try again:\n')

        return render_template("form.html", guess=guess, min=min, max=max)




app.run(debug=True)