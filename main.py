import webapp2
import random

class Index(webapp2.RequestHandler):
    def get(self):
        header = '<h1>Signup</h1>'
        username_line = 'Username: <input type="text" name="username"><br>'
        password1_line = 'Password: <input type="password" name="password"><br>'
        password2_line = 'Confirm Password: <input type="password" name="password-confirm"> <br>'
        email_line = 'Email (optional): <input type="text" name="email">'
        signup_form = "<form>" +  username_line + password1_line + password2_line + email_line + "</form>"
        submit_button ='<input type="submit">'
        content = header + signup_form + submit_button
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
