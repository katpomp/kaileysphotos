from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def mommy():
    return render_template('index.html')


@app.route('/football')
def football():
    return render_template('football.html')


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')


if __name__ == "__main__":
    app.run()
