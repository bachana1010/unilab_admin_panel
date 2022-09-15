from flask import Blueprint, flash, url_for, \
    redirect, render_template, request, session
from flask_login import logout_user, login_required, current_user

from app.auth.forms import RegisterForm, LoginForm
from app.auth.models import User
from app import db

user_blueprint = Blueprint('user', __name__, template_folder="templates")

@user_blueprint.route('/')
def home():
    return render_template("base.html")


@user_blueprint.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
            user = User(
                name = form.first_name.data,
                last_name = form.last_name.data,
                email = form.email.data,
                gender = form.sex.data,
                birth_date = form.birth_date,
                mobile_number = form.phone_number.data,
                passport_id = form.personal_id.data,
                country = form.country.data,
                city = form.city.data,
                region = form.region.data,
                address = form.address.data,
                role = form.status.data
            )

            db.session.add(user)
            db.session.commit()
            flash("რეგისტრაცია წარმატებით დასრულდა")
            return redirect(url_for('user.login'))
    return render_template("registration.html", form = form)

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
                user = User.find_by_email(form.email.data)
                session["logged_in"] = True


                if user is not None:
                    login_user(user)
                    flash("მომხმარებელმა წარმატებით გაიარა ავტორიზაცია")


                    # next = request.args.get('next')
                    #
                    # if next is None:
                    #     next = url_for('unilab.main')
                    #
                    # return redirect(next)

    return render_template("login.html", form = form)



@user_blueprint.route('/welcome', methods=['GET', 'POST'])
@login_required
def welcome():

    return render_template("welcome.html")

# @user_blueprint.route('/logout', methods=['GET'])
# def logout():
#     logout_user()
#     flash("მომხმარებელი გამოვიდა სისტემიდან")
#     session["logged_in"] = False
#     return render_template("base.html")
#

