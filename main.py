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

@app.route('/springsports')
def spring():
    return render_template('springsports.html')


@app.route('/nature')
def nature():
    return render_template('nature.html')


@app.route('/wintersports')
def winter():
    return render_template('/wintersports.html')


if __name__ == "__main__":
    app.run()
# >>>>>>> 6fc044846db19f7f8f89c6b3b746b9bd54635921
