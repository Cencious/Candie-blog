from flask import render_template,redirect,url_for,flash,request
from ..models import User, Subscriber, Post
from .forms import LoginForm, RegistrationForm, SubscriberForm
from .. import db
from . import auth
from ..email import mail_message
from flask_login import login_user,logout_user,login_required, current_user
