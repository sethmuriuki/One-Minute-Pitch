from flask import render_template,redirect,url_for,request,flash
from . import auth
from flask_login import login_user,logout_user,login_required
from .. model import User
from . forms import RegistrationForm,LoginForm
from .. import db

#registration route

@auth.route('/register',method = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data)
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next')or url_for('main.index'))

        flash('invalid password')

    title = "One Minute Pitch Login"
    return render_template('auth/login.html',login_form = login_form,title = title)
