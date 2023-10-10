from flask import Flask,render_template,request
import numpy as np



app = Flask(__name__)

@app.route("/",methods = ['POST','GET'])
def hello_world():
    return render_template("index.html")

@app.route("/math",methods = ['POST'])
def math_operations():

    ops = request.form["operation"]
    num1 = int(request.form["num1"])
    num2 = int(request.form['num2'])

    if ops == "add":
        result = f"The sum of {num1} and {num2} will be :- {num1+num2} "   
    
    if ops == "subtract":
        result = f"The subtract of {num1} and {num2} will be :- {num1-num2} "
    
    if ops == "multiply":
        result = f"The multiply of {num1} and {num2} will be :- {num1*num2} "

    if ops == "divide":
        result = f"The divide of {num1} and {num2} will be :- {num1/num2} "
    
    if ops == 'log':
        result = f" log{num1}  ->   {np.log2(num1)}  ||  log{num2}  ->   {np.log2(num2)}  "
    
    if ops == 'log10':
        result = f" log{num1}  ->   {np.log10(num1)}  ||  log{num2}  ->   {np.log10(num2)}  "
    
    if ops =='squre':
        result = f"squre {num1} -> {np.square(num1)}  ||  squre {num2}  ->  {np.square(num2)} "
    
    if ops=="sqr":
        result = f"squre root {num1}  -> {np.sqrt(num1)}  ||  squre root {num2}  ->  {np.sqrt(num2)} "
    

    return render_template("results.html",result = result)

if __name__=="__main__":
    app.run(host="0.0.0.0")
