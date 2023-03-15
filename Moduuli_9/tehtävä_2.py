"""
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h
ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.

"""

class Car:
    def __init__(self,reg_number, top_speed, current_speed, distance_traveled):
        self.reg_number = reg_number
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



car1 = Car("ABC-123", 142, 0, 0)
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(f"Car's current speed: {car1.current_speed} km/h.")
car1.accelerate(-200)
print(f"Car's current speed: {car1.current_speed} km/h. ")