from flask import Flask
from codify import *


app = Flask(__name__)


@app.route('/post/<string:i>', methods=['POST'])
def post_str_req(i):
    return {"Key": f"This is a post request with passed parameter {i}"}


@app.route('/post/<int:i>', methods=['POST'])
def post_req(i):
    return {"Key": f"This is a post request with passed parameter {i}"}

# just go in the postman type this url and click in send


@app.route('/post', methods=['POST'])
def simple_post_req():
    return {"Key": "This is a post request with no passed parameter"}


@app.route('/', methods=['GET'])
def home():
    return "This is get request!"


# other request: put and delete
if __name__ == '__main__':
    app.run(debug=True)
