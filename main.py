from flask import Flask, Blueprint, request, redirect, render_template, url_for


main = Blueprint('main', __name__)



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/')
def profile():
    return render_template('profile.html')