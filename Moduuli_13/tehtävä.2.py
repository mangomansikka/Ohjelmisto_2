"""
Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen
ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
"""

import mysql.connector
from flask import Flask, Response, jsonify
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='cindy',
    password='5206xx',
    autocommit=True
    )

def get_airport(icao):
    sql = "SELECT name, municipality FROM airport WHERE ident='" + icao + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

@app.route('/kenttä/<icao>')
def airport(icao):
    result = get_airport(icao)
    answer = {
        "ICAO" : icao,
        "Name" : result[0],
        "Municipality" : result[1]

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