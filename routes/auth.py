from flask import Blueprint, render_template,request
from lib.validators.signup_validator import SignupValidator

auth = Blueprint('auth', __name__, url_prefix='/auth')
signup = SignupValidator()

@auth.route('/login')
def login_form():
    return render_template('login_form.html')

@auth.route('/signup')
def signup_form():
    return render_template('signup.html')

@auth.route('/signup-conf', methods=['GET','POST'])
def signup_conf():
    password = request.form['password']
    confpassword = request.form['confirmpassword']

    conf = signup.is_valid(password,confpassword)

    if(conf == 1):
        return render_template('signup_complete.html')
    else:
        return render_template('signup.html')
    


