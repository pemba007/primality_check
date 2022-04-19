from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def hello_world():
    print("Hello world is running")
    return "<p>Hello, World!</p>"


@app.route("/test")
def testing_function():
    print("Testing function is running")
    return "<p>Fuck You it works!</p>"


@app.route("/checkPrime")
@cross_origin()
def prime():
    n = int(request.args.get('numberToCheck'))
    
    # 0, 1, even numbers greater than 2 are NOT PRIME
    if n==1 or n==0 or (n % 2 == 0 and n > 2):
        return jsonify(answer="False")
    else:
        # Not prime if divisable by another number less
        # or equal to the square root of itself.
        # n**(1/2) returns square root of n
        for i in range(3, int(n**(1/2))+1, 2):
            if n%i == 0:
                return jsonify(answer="False")
        return jsonify(answer="True")