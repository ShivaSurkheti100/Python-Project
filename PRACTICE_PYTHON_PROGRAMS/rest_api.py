### create a rest API using Flask and Jsonify in Python
## below program is not working ::::::

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/armstrong/<int:n>')
def armstrong(n):
    n = int(input("Enter a number: "))
    sum = 0
    order = len(str(n))
    copy_n = n ## while loop exit garda n=0 hunxa so we need copy of n
    while(n>0):
        digit = n % 10 # digit = x
        sum += digit**order ## x^n
        n = n // 10

    if sum == copy_n :
        print(f"{copy_n} is an Armstrong number")
        result = {
            "number": copy_n, 
            "armstrong" : True, 
            "Server IP": "122.234.213.53"
        }
    else:
        print(f"{copy_n} is not an Armstrong number.")
        result = {
            "number": copy_n, 
            "armstrong" : False, 
            "Server IP": "122.234.213.53"
        }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)



# Yettikai gareko ho talako
# def sum(a, b):
#     return a+b
# def average(a, b):
#     return (a+b)/2