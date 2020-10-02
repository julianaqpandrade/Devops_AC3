import os
from flaks import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')

def primos():
    lim = 100
    num = 3
    a = 1
    
    primo = '2, '
    
    while p < lim:
        nprimo = 1
        for i in range(2, num):
            if num % == 0:
                nprimo = 0
                break
        if(nprimo):
            primo = primo + str(num) + ','
            a += 1
            if(p % 10 == 0):
                primo += '<br>'
            num += 1
    return primo

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)
