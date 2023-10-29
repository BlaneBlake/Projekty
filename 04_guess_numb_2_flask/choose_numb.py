from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/guess/" methods=["GET", "POST"])
def guess_number():
    if request.method == "GET:":
        return render_template("form.html" min=0, max=1000)
    min = 0
    max = 1000
    answer = "None"

    args = request.args

    while answer != "You win":

        guess = (max - min) // 2 + min


        min = args.get("min")
        max = args.get("max")
        answer = args.get("answer")

        if answer == "You won":
            return render_template("win.html", guess=guess)
        elif answer == "Too small":
            min = guess

        elif answer == "Too big":
            max = guess
        return render_template("form.html", guess=guess, min=min, max=max) + render_template("choose.html")




app.run(debug=True)