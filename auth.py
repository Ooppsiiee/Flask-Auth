from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import DataUser
import uuid

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_POST():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    unique_key = str(uuid.uuid4())
    User = DataUser.query.filter_by(email=email).first()

    if User:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    new_user = DataUser(email, username, generate_password_hash(password, method='sha256'), unique_key)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))