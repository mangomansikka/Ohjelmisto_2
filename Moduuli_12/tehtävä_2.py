"""
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan
tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi.
Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

"""

import json
import requests

search = input("Anna kaupungin nimi: ")

request = "https://api.openweathermap.org/data/2.5/weather?q=" + search + "&appid=b8c98e2ca84aff04cc1dbfa5e21b5aa9"

try:
    answer = requests.get(request)
    if answer.status_code == 200:
        json_answer = answer.json()
        weather = json_answer['weather'][0]['description']
        celcius = round(json_answer['main']['temp'] - 273.15)
        print(f"Sää: {weather}.")
        print(f"Lämpötila: {celcius} celciusta.")

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
