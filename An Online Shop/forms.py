from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, EmailField, PasswordField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired()])
    name = StringField(label="Name", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField('Sign Me Up')


class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField('Login')
