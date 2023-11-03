from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def guess_number():
    if request.method == "GET":
        return render_template("form.html", min='0', max='1000')
    else:
        form = request.form
        min = int(form["min"])
        max = int(form["max"])
        # answer = form["answer"]
        # guess = form["guess", 500] # guess = (max - min) // 2 + min zamienic 500 na wzor jesli pobierze inne zmienne
        answer = form.get("answer")
        guess = int(form.get("guess", (max - min) // 2 + min))

        if answer == "You won":
            return render_template("win.html", guess=guess)
        elif answer == "Too small":
            min = guess

        elif answer == "Too big":
            max = guess

        guess = (max - min) // 2 + min
        return render_template("choose.html", guess=guess, min=min, max=max)




app.run(debug=True)