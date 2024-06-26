from flask import Flask

# Create a Flask application object named 'app'
app = Flask(__name__)


# Define a route for '/airbnb-onepage/'
@app.route('/airbnb-onepage/')
def hello():
    return 'Hello HBNB!'


# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
