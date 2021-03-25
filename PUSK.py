from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import os
import os.path

UPLOAD_FOLDER = '/presentations'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['POST', 'GET'])
@app.route('/start', methods=['POST', 'GET'])
def start():
    return render_template("start.html")


@app.route('/pattern', methods=['POST', 'GET'])
def pattern():
    if request.method == 'POST':
        if request.form.get('1') == "1":
            return send_from_directory(directory="presentations", filename="algebra.pptx", as_attachment=True)
        if request.form.get('2') == "2":
            return send_from_directory(directory="presentations", filename="Russian.pptx", as_attachment=True)
        if request.form.get('3') == "3":
            return send_from_directory(directory="presentations", filename="chemistry.pptx", as_attachment=True)
    return render_template("pattern.html")


@app.route('/check', methods=['POST', 'GET'])
def check():
    if request.method == 'POST':
        file = request.files['file']
        file.save("files/" + file.filename)
        return redirect("/response/" + file.filename)
    return render_template("check.html")

@app.route('/response/<file>', methods=['POST', 'GET'])
def response(file):
    if file == "kreativnost.pptx":
        return render_template("response.html")
    return redirect("/check")


@app.route('/recommendation', methods=['POST', 'GET'])
def recommendation():
    return render_template("recommendation.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
