from flask import Flask

'''
   It creates a new instance of Flask class,
   which will be your WSGI(Web Server Gateway Interface) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to the Flask"

@app.route("/Index")
def index():
    return "Welcome to the Index"

@app.route("/Home")
def home():
    return "Welcome to the Home"

if __name__ == '__main__':
    app.run(debug=True)

