from flask import Flask, render_template, request

# Create a Flask instance
app = Flask(__name__)


#home page
@app.route("/")
def HelloWorld():
    return "Hello World, welcome to Flask!"

#profile page
@app.route("/profile")
def profile():
    user = {
        "username": "John Doe",
        "age": 25,
        "Bio": "I am a Machine Learning Engineer"
    }

    return render_template("profile.html", name=user["username"], age=user["age"], bio=user["Bio"])

#form page
@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

#submit page
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Hello {name}, welcome to Flask!"
# Create a route
if __name__ == "__main__":
    app.run(debug=True)
