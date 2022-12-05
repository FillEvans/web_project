from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home():
    return render_template("test.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/enroll')
def enroll():
    return render_template("enroll.html")


if __name__ == "__main__":
    app.run(debug=True)