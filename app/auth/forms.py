from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    '''
    registrationform class that passes in the required and email validators
    '''

    email = StringField('your email address',validators = [Required(),Email()])
    username = StringField('your username', validators = [Required()])
    password = PasswordField('password',validators = [Required(),EqualTo('password'message = 'passwords must match')])
    password_confirm = PasswordField('confirm your password',validators=[Required()])
    submit = SubmitField('sign up')

    #custom validators
    def validate_email(self,data_field):
        '''
        Functions takes in the data field and checks our database to confirm user Validation
        '''
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('An account in that email already exists')

    def validate_username(self,data_field):
        '''
        Function checks if the username is unique and raises ValidationError
        '''
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('that name is already taken')


# Login form with 3 fields
class LoginForm(FlaskForm):
    email = StringField('your email address',validators=[Required(),Email()])
    password = PasswordField('password',validators=[Required()])
    remember = BooleanField('keep password')
    submit = SubmitField('sign in')