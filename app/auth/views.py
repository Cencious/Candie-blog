from flask import render_template,redirect,url_for,flash,request
from ..models import User, Subscriber, Post
from .forms import LoginForm, RegistrationForm, SubscriberForm
from .. import db
from . import auth
from ..email import mail_message
from flask_login import login_user,logout_user,login_required, current_user

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to Candie Blog","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form=form)

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Candie Blog login"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/subscribe', methods=['GET','POST'])
def subscriber():
    subscriber_form = SubscriberForm()
    if subscriber_form.validate_on_submit():

        blogs = Post.query.order_by(Post.date_created.desc()).all()
        subscriber = Post.query.all()

        blogs = Post.query.all()

        subscriber= Subscriber(email=subscriber_form.email.data,name = subscriber_form.name.data)

        db.session.add(subscriber)
        db.session.commit()

        mail_message("Welcome to Candie Blog","email/welcome_subscriber",subscriber.email,subscriber=subscriber)

        title = "Candie Blog"

        return redirect(url_for('main.blog', title=title, blogs=blogs, subscriber_form=subscriber_form))


