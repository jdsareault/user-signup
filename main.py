import webapp2
from signup_validation import validate_username, validate_password, validate_email

content = '''
<head>
    <style type="text/css">
      .error {color: red}
    </style>
</head>
<body>
    <h1>Signup</h1>
    <form method="post">
        Username: <input type="text" name="username" value=""><span class="error">%(usererror)s</span><br>
        Password: <input type="password" name="password"><span class="error">%(passworderror)s</span><br>
        Confirm Password: <input type="password" name="password-confirm"><br>
        Email (optional): <input type="text" name="email" value=""><span class="error">%(emailerror)s</span><br>
        <input type="submit">
    </form>
</body>
'''

errors = {'usererror' : "", 'passworderror' : "", 'emailerror' : ""}

class Signup(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(content % errors)
        print("Program is getting")

    def post(self):
        print("Program is posting")
        valid_name = validate_username(self.request.get("username"))
        print("valid_name = ", valid_name)
        valid_password = validate_password(self.request.get("password"),self.request.get("password-confirm"))
        print("valid_password = ", valid_password)
        valid_email = validate_email(self.request.get("email"))
        print("valid_email = ", valid_email)

        if not valid_name:
            errors['usererror'] = "Invalid Username"
#        else:
#            errors['usererror'] = ""
        if not valid_password:
            errors['passworderror'] = "Invalid Password"
#        else:
#            errors['passworderror'] = ""
        if not valid_email:
            errors['emailerror'] = "Invalid Email"
#        else:
#            errors['emailerror'] = ""

        if not (valid_name and valid_password and valid_email):
            self.response.out.write(content % errors)
            errors['usererror'] = ""
            errors['passworderror'] = ""
            errors['emailerror'] = ""

        else:
            self.response.out.write("Confirm!")

class Welcome(webapp2.RequestHandler):
    def get(self):
        print("Welcome Get")
    def post(self):
        print("Welcome Post")

app = webapp2.WSGIApplication([
    ('/', Signup),
    ('/signup', Signup),
    ('/welcome',Welcome)
], debug=True)
