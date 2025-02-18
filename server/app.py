#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)



@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:text>")
def print_string(text):
    print(text)
    return text

@app.route("/count/<int:number>")
def count(number):
    numbers = "\n".join(str(i) for i in range(number)) + "\n"
    print(numbers)
    return numbers

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, num2, operation):
    if operation == "+":
        result = str(num1 + num2)
    elif operation == "-":
        result = str(num1 - num2)
    elif operation == "*":
        result = str(num1 * num2)
    elif operation == "div":
        result = str(num1 / num2)
    elif operation == "%":
        result = str(num1 % num2)
    else:
        result = "INVALID OPERATOR"
    
    print(result)
    return result