from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def mommy():
    return render_template('index.html')


@app.route('/fallsports')
def fall():
    return render_template('/fall/fallsports.html')


@app.route('/football')
def football():
    return render_template('/fall/football.html')


@app.route('/cheerleading')
def cheerleading():
    return render_template('/fall/cheerleading.html')


@app.route('/volleyball')
def volleyball():
    return render_template('/fall/volleyball.html')


@app.route('/springsports')
def spring():
    return render_template('/spring/springsports.html')


@app.route('/other')
def other():
    return render_template('/other/other.html')


@app.route('/wintersports')
def winter():
    return render_template('/winter/wintersports.html')


@app.route('/baseball')
def baseball():
    return render_template('/spring/baseball.html')


@app.route('/boysbasketball')
def boysbasketball():
    return render_template('/winter/boysbasketball.html')


@app.route('/boyslacrosse')
def boyslacrosse():
    return render_template('/spring/boyslacrosse.html')


@app.route('/boyssoccer')
def boyssoccer():
    return render_template('/spring/boyssoccer.html')


@app.route('/girlslacrosse')
def girlslacrosse():
    return render_template('/spring/girlslacrosse.html')


@app.route('/girlssoccer')
def girlssoccer():
    return render_template('/spring/girlssoccer.html')


@app.route('/animals')
def animals():
    return render_template('/other/animals.html')


@app.route('/softball')
def softball():
    return render_template('/spring/softball.html')


@app.route('/flowers')
def flowers():
    return render_template('/other/flowers.html')


if __name__ == "__main__":
    app.run()
