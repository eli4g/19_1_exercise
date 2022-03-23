# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)


@app.route("/add")
def addition():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    return str(result)

@app.route("/sub")
def subtraction():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return str(result)

@app.route("/mult")
def multiplication():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return str(result)


@app.route("/div")
def division():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return str(result)



@app.route("/math/<calc_type>")
def do_math(calc_type):
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    
    do_math_type = {"add": add(a,b), "sub": sub(a,b), "mult": mult(a,b), "div": div(a,b)}
    
    
    result = do_math_type[calc_type]
    
    return str(result)