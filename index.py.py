from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ---- Login Route ----
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "iloveyou" and password == "pandi":
            return redirect(url_for('proposal'))
        else:
            return render_template("index.html", error="Invalid username or password")

    return render_template("index.html")


# ---- Proposal Page ----
@app.route('/proposal')
def proposal():
    return render_template("proposal.html")


# ---- Video Page ----
@app.route('/video')
def video():
    return render_template("love.html")


if __name__ == '__main__':
    app.run(debug=True)
