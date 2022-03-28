from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def mommy():
    return render_template('index.html')


@app.route('/fallsports')
def fall():
    return render_template('fallsports.html')


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')


@app.route('/football')
def football():
    return render_template('football.html')


@app.route('/cheerleading')
def cheerleading():
    return render_template('cheerleading.html')


@app.route('/volleyball')
def volleyball():
    return render_template('volleyball.html')


>>>>>>> 6b7c3b34519a72fe26a0c26b6543ac67545bc41d
@app.route('/springsports')
def spring():
    return render_template('springsports.html')


@app.route('/other')
def other():
    return render_template('other.html')


@app.route('/wintersports')
def winter():
    return render_template('/wintersports.html')


@app.route('/baseball')
def baseball():
    return render_template('/baseball.html')


@app.route('/boysbasketball')
def boysbasketball():
    return render_template('/boysbasketball.html')


@app.route('/boyslacrosse')
def boyslacrosse():
    return render_template('/boyslacrosse.html')


@app.route('/boyssoccer')
def boyssoccer():
    return render_template('/boyssoccer.html')


@app.route('/girlslacrosse')
def girlslacrosse():
    return render_template('/girlslacrosse.html')


@app.route('/girlssoccer')
def girlssoccer():
    return render_template('/girlssoccer.html')


@app.route('/animals')
def animals():
    return render_template('/animals.html')

@app.route('/softball')
def softball():
    return render_template('/softball.html')

@app.route('/flowers')
def flowers():
    return render_template('/flowers.html')


if __name__ == "__main__":
    app.run()
