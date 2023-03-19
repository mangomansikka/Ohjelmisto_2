"""
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja,
joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.
Luokassa on seuraavat metodit:
tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on
ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen,
kun kilpailu on päättynyt.

"""

import random

class Car:
    def __init__(self,reg_number, top_speed, current_speed, distance_traveled):
        self.reg_number = f"ABC-{reg_number}"
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.distance_traveled = distance_traveled
        self.status = False
        self.hours_driven = 0
    def accelerate(self, velocity):
        if velocity > 0:
            self.current_speed += velocity
            if self.current_speed + velocity > self.top_speed:
                difference = self.current_speed - self.top_speed
                self.current_speed -= difference
        else:
            self.current_speed += velocity
            if self.current_speed + velocity < 0:
                difference = velocity + self.current_speed
                velocity -= difference
                self.current_speed += velocity
    def drive(self, hours):
        self.distance_traveled += self.current_speed * hours

class Competition:
    def __init__(self, name, distance, car):
        self.name = name
        self.distance = distance
        self.cars = []
        self.cars.append(car)

    def hour_passes(self, car):
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        car.hours_driven += 1

    def print_status(self, value):
        print("--------------------------------")
        print(f"Registration number: {value.reg_number}")
        print(f"Top speed: {value.top_speed}")
        print(f"Current speed: {value.current_speed}")
        print(f"Distance traveled: {value.distance_traveled}")
        print(f"Goal: {value.status}")

    def competition_over(self, car):
        if car.distance_traveled >= self.distance:
            car.status = True



cars = []
competitors = 0
competitions = True

while competitors <= 9:
    competitors = competitors + 1
    number = competitors
    cars.append(Car(number, random.randint(100, 200), 0, 0))

while competitions:
    for value in cars:
        participants = Competition("Suuri romuralli", 8000, value)
        if value.hours_driven == 10:
            participants.print_status(value)
        participants.hour_passes(value)
        participants.competition_over(value)
        if value.status:
            competitions = False
            for value in cars:
                participants.print_status(value)

print("--------------------------------")
print("The competition has finished!")

winner = 0
winners = {}
distances = []

for car in cars:
    if car.status:
        distance = car.distance_traveled
        registration = car.reg_number
        distances.append(distance)
        winner = max(distances)
        winners[winner] = registration

print(f"The winner {winners[winner]} has traveled {winner} kilometers. {winners[winner]} is the fastest car!")

