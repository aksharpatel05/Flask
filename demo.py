from flask import Flask

# Create a Flask instance
app = Flask(__name__)


@app.route("/")
def HelloWorld():
    return "Hello World, welcome to Flask!"

#index page
@app.route("/index")
def index():
    return "Welcome to the index page!"


# Create a route
if __name__ == "__main__":
    app.run(debug=True)
