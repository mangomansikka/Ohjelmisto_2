"""
Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja,
joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

"""

class Car:
    def __init__(self,reg_number, top_speed, current_speed, distance_traveled):
        self.reg_number = reg_number
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.distance_traveled = distance_traveled

car1 = Car("ABC-123", "142 km/h", 0, 0)

print(f"Car's registration number: {car1.reg_number}, top speed:{car1.top_speed}, "
      f"current speed: {car1.current_speed}, distance traveled: {car1.distance_traveled}")



