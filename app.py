# coding: utf-8
 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    print("DEBUG: Reached to main()")
    return 'Hello world!'
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
