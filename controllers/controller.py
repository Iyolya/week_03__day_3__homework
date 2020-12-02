from app import app
from modules.calculator import *


@app.route ('/add/<num1>/<num2>')
def call_add(num1, num2):
    return add(num1, num2)

@app.route ('/subtract/<num1>/<num2>')
def call_subtract(num1, num2):
    return subtract(num1, num2)

@app.route ('/multiply/<num1>/<num2>')
def call_multiply(num1, num2):
    return multiply(num1, num2)

@app.route ('/divide/<num1>/<num2>')
def call_divide(num1, num2):
    return divide(num1, num2)






