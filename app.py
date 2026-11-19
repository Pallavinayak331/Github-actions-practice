# this is simple python app code
from flask import Flask

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
  
