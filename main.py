"""
    Read https://flask-wtf.readthedocs.io/en/1.0.x/form/ and use it to figure out how to create a simple login form.

    In Pycharm Go to File>Settings>Project: myProjectName>Python Interpreter.
    Clik the + sign and type Flask-WTF to get the module and install it.

    https://wtforms.readthedocs.io/en/2.3.x/crash_course/#validators
    https://pythonhosted.org/Flask-Bootstrap/basic-usage.html

    pip install Flask-WTF
    pip install email-validator
    pip install Flask-Bootstrap

    https://pythonhosted.org/Flask-Bootstrap/forms.html

    solution:
    https://gist.github.com/angelabauer/162f56578b9193090963a0691c826790
    https://gist.github.com/angelabauer/e5b1a26a79888f67b490c1f53ed2496c
"""
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)

class LoginForm(FlaskForm):
    #    https://wtforms.readthedocs.io/en/2.3.x/crash_course/#validators
    email = StringField(label='Email', validators=[DataRequired(), validators.Length(min=4, max=120), validators.Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), validators.Length(min=8, max=120)])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.email.data)

        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)