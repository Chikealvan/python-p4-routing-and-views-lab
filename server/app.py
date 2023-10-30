#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Print the string to the console
    return param  # Display the string in the web browser

@app.route('/count/<int:param>')
def count(param):
    numbers = "\n".join(str(i) for i in range(param))
    return numbers

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return f"{num1} {operation} {num2} = {result}"
    else:
        return "Invalid operation. Supported operations: +, -, *, div, %"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
