"""
Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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
    def drive(self, hours):
        self.distance_traveled += self.current_speed * hours



car1 = Car("ABC-123", 142, 60, 2000)
car1.drive(1.5)

print(f"The car has traveled {car1.distance_traveled} km. ")