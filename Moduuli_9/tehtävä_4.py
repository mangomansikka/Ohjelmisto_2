"""

Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna

"""
import random

class Car:
    def __init__(self,reg_number, top_speed, current_speed, distance_traveled):
        self.reg_number = f"ABC-{reg_number}"
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.distance_traveled = distance_traveled
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

cars = []
competitors = 0
competition = True

while competitors <= 9:
    competitors = competitors + 1
    number = competitors
    cars.append(Car(number, random.randint(100, 200), 0, 0))

while competition:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.distance_traveled >= 10000:
            competition = False

print("The competition is finished!")
distances = []
winners = {}
winner = 0
for car in cars:
    print("--------------------------------")
    print(f"Registration number: {car.reg_number}")
    print(f"Top speed: {car.top_speed}")
    print(f"Current speed: {car.current_speed}")
    print(f"Distance traveled: {car.distance_traveled}")
    if car.distance_traveled >= 10000:
        distance = car.distance_traveled
        registration = car.reg_number
        distances.append(distance)
        winner = max(distances)
        winners[winner] = registration

print("--------------------------------")
print(f"The winner {winners[winner]} has traveled {winner} kilometers. {winners[winner]} is the fastest car!")
