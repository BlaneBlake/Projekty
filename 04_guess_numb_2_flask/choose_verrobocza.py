from flask import Flask, request, render_template
app = Flask(__name__)

HTML_Form = """
<html lang="en">
    <body>
        <h1>Imagine number between 0 and 1000</h1>
        <form action="" method="POST">
            <input type="hidden" id="min" name="min" value="{}">
            <input type="hidden" id="max" name="max" value="{}">
            <input type="submit" value="OK">
        </form>
    </body>
</html>"""
HTML_Win = """
<html lang="en">

<body>
<p>I win, you choose {{guess}}</p>
</body>
</html>"""
HTML_Choose = """
<html lang="en">

    <body>
        <h1>I guess: {{guess}}</h1>
        <form action="" method="POST">
            <input class="button" type="submit" id="answer" name="answer" value="You won">
            <input class="button" type="submit" id="answer" name="answer" value="Too small">
            <input class="button" type="submit" id="answer" name="answer" value="Too big">

            <input type="hidden" name="min" value="{min}">
            <input type="hidden" name="max" value="{max}">
            <input type="hidden" name="guess" value="{guess}">

        </form>
    </body>
</html>"""
@app.route("/guess/", methods=["GET", "POST"])
def guess_number():
    if request.method == "GET:":
        return HTML_Form.format(0, 1000)
    else:

        form = request.form

        min = int(form.get("min"))
        max = int(form.get("max"))
        guess = int(form.get("guess", 500))
        answer = form.get("answer")

        if answer == "You won":
            return HTML_Win.format(guess=guess)
        elif answer == "Too small":
            min = guess
        elif answer == "Too big":
            max = guess
        return HTML_ChooseHTML.format(guess=guess, min=min, max=max)



app.run(debug=True)