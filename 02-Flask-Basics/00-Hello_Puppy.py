from flask import Flask
from pyfuncs import *
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'
@app.route('/page1')
def pages():
    return '<h1>Hello page1!</h1>'
@app.route('/puppy/<name>')
def puppy(name):
    new_string = namLatin(name)
    x = read_data()
    return x
if __name__ == '__main__':
    app.run(debug=True)
