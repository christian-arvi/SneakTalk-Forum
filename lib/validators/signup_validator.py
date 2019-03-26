class SignupValidator:
    def __init__(self):
        print('Signup validator instantiated')

    def is_valid(self,password,confpassword):
        if(password == confpassword):
            return 1
            
        else:
            return 0