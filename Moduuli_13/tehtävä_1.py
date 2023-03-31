"""
Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31
vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
"""

from flask import Flask, Response, jsonify
import json

app = Flask(__name__)

def is_prime(n):
    answer = True
    for i in range(2, n):
        if n % i == 0:
            answer = False
    return answer

@app.route('/alkuluku/<int:n>')
def prime(n):
    result = is_prime(n)
    answer = {
        "Number": n,
        "isPrime": result
    }
    return jsonify(answer)

@app.errorhandler(404)
def page_not_found(error_code):
    answer = {
        "status" : "404",
        "text" : "False end point"
    }
    jsonanswer = json.dumps(answer)
    return Response(response=jsonanswer, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)