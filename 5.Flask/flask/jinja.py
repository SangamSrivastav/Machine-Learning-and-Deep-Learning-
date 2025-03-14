### Building url dynamically
## Variable rule
### Jinja 2 template Engine

from flask import Flask, render_template,request,redirect,url_for

'''
   It creates a new instance of Flask class,
   which will be your WSGI(Web Server Gateway Interface) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route("/")
def Welcome():
    return "<html><H1>Welcome to the Flask Course</H1></html>"

@app.route("/Index",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")






## variable rule
@app.route('/success/<int:score>')
def success(score):
    return f"Congratulations! You scored {score}" + str(score)

@app.route('/forloop/<int:score>')
def forloop(score):
    res=""
    if score>50:
        res="Passed"
    else:
        res="Failed"

    exp = {"score":score,"res":res}

    return render_template("forloop.html",results=exp)

@app.route('/ifloop/<int:score>')
def ifloop(score):

    return render_template("res.html",results=score)

@app.route("/submit", methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            science = float(request.form['science'])
            maths = float(request.form['maths'])
            c = float(request.form['c'])
            data_science = float(request.form['datascience'])

            total = (science + maths + c + data_science) / 4
            return redirect(url_for('forloop', score=total))
        except ValueError:
            return "Invalid input! Please enter numeric values."

    # If it's a GET request, render the form
    return render_template("getresult.html")


@app.route("/Home")
def home():
    return "Welcome to the Home"

if __name__ == '__main__':
    app.run(debug=True)

