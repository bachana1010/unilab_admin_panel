from sqlite3 import register_converter
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,EmailField,PasswordField,SelectField,DateField,TelField,IntegerField,BooleanField
from wtforms.validators import DataRequired,Email, Length,ValidationError



class RegisterForm(FlaskForm):
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email):
        email_address = User.query.filter_by(email=email.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    def validate_personal_id(self,personal_id):
        personal_id = personal_id.data
        if  not personal_id.is_numeric():
            raise ValidationError('Personal ID Should be numbers')
        personal_id = User.query.filter_by(personal_id=personal_id.data).first()
        if personal_id:
            raise ValidationError('Personal ID already exists! Please check and try again!')

    username = StringField('Username',[Length(min=2, max=30),DataRequired()])
    first_name = StringField('First Name',[DataRequired()])
    last_name = StringField('Last Name',[DataRequired()])
    email = EmailField('Email',[Email(),DataRequired()])
    sex = SelectField(u'Sex',[DataRequired()], choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    birth_date = DateField('Birth Date',[DataRequired()])
    phone_number = TelField('Phone Number',[DataRequired()])
    personal_id = IntegerField('ID Number',[Length(min=11,max=11),DataRequired()])
    country = StringField('Country',[DataRequired()])
    region = StringField('Region',[DataRequired()])
    city = StringField('City',[DataRequired()])
    address = StringField('Address',[DataRequired()])
    status = SelectField(u'Choose Your Status',[DataRequired()], choices=[('pupil', 'მოსწავლე'), ('student', 'სტუდენტი'), ('other', 'სხვა')])
    submit = SubmitField('Create Account')


class LoginForm(FlaskForm):
    email = EmailField('Email',validators=[Email(),DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    # forget_password =
    submit = SubmitField("Sign in")