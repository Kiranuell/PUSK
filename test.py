from flask import Flask, render_template, request, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class StartForm(FlaskForm):
    submit = SubmitField('sub')


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/start', methods=['POST', 'GET'])
def start():
    return render_template("start.html")


@app.route('/pattern', methods=['POST', 'GET'])
def pattern():
    if request.method == 'POST':
        if request.form.get('1') == "1":
            return send_from_directory(directory="static", filename="image/sera.jpg", as_attachment=True)
        if request.form.get('2') == "2":
            return send_from_directory(directory="static", filename="image/lucifer.jpg", as_attachment=True)
        if request.form.get('3') == "3":
            return send_from_directory(directory="static", filename="image/raphael.jpg", as_attachment=True)
    return render_template("pattern.html")


@app.route('/check', methods=['POST', 'GET'])
def check():
    return render_template("check.html")


# @app.route('/check/response', methods=['POST', 'GET'])
# def check():
#     return render_template("check.html")


@app.route('/recommendation', methods=['POST', 'GET'])
def recommendation():
    return render_template("recommendation.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
