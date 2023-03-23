"""
Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
Käyttäjälle on näytettävä pelkkä vitsin teksti.

"""


import requests

request = "https://api.chucknorris.io/jokes/random"

try:
    answer = requests.get(request)
    if answer.status_code==200:
        json_answer = answer.json()
    print("Here is a Chuck Norris joke for you. You welcome!")
    print(json_answer["value"])

except requests.exceptions.RequestException as e:
    print("We couldn't complete the search.")
