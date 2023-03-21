"""
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen,
huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi
sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton
(ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja
tulosta autojen matkamittarilukemat.
"""

import random

class Car:

    cars = 0

    def __init__(self, reg_number, top_speed, capacity, current_speed):
        self.reg_number = f"ABC-{reg_number}"
        self.top_speed = top_speed
        self.capacity = capacity
        self.current_speed = current_speed
        self.distance_traveled = 0
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
        self.hours_driven += hours

    def print(self):
        print("--------------------------------")
        print(f"Registration number: {self.reg_number}")
        print(f"Top speed: {self.top_speed}")
        print(f"Current speed: {self.current_speed}")
        print(f"Hour's driven: {self.hours_driven}")
        print(f"Distance traveled: {self.distance_traveled}")
        print("--------------------------------")


class Electric_car(Car):
    def __init__(self, reg_number, top_speed, battery_capacitykw):
        self.reg_number = f"ABC-{reg_number}"
        self.top_speed = top_speed
        self.battery_capacity = f"{battery_capacitykw} + kw"
        super().__init__(reg_number, top_speed, battery_capacitykw, random.randint(0, top_speed))

class Engine_car(Car):

    def __init__(self, reg_number, top_speed, gas_tankl):
        self.reg_number = f"ABC-{reg_number}"
        self.top_speed = top_speed
        self.gas_tank = f"{gas_tankl} + l"
        super().__init__(reg_number, top_speed, gas_tankl, random.randint(0, top_speed))


el_car1 = Electric_car(15, 180, 52.5)
en_car1 = Engine_car(123, 165, 32.3)
el_car1.drive(3)
en_car1.drive(3)
el_car1.print()
en_car1.print()