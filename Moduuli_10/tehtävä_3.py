"""
Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

"""


elevator_list = []


class Elevator:
    def __init__(self, bot_floor, top_floor):
        self.bot_floor = bot_floor
        self.top_floor = top_floor
        self.current_floor = bot_floor

    def move_to(self, floor):
        self.current_floor = floor
        print(f"The elevator is on floor {floor}.")

    def one_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor = self.current_floor + 1
            print(f"The elevator is on floor {self.current_floor}.")
        else:
            print("The elevator is on the highest floor. It can't go up.")

    def one_down(self):
        if self.current_floor != 1:
            self.current_floor = self.current_floor - 1
            print(f"The elevator is on floor {self.current_floor}.")
        else:
            print("The elevator is on the lowest floor. It can't go down. ")


class House:
    def __init__(self, bot_floor, top_floor, elevators):
        self.bot_floor = bot_floor
        self.top_floor = top_floor
        self.elevators = elevators

    def move(self, elevator, floor):
        elevator_list[elevator].move_to(floor)

    def fire_alarm(self):
        print("RIINGGGG there is a fire! All elevators are moved to the bottom floor!")
        for elevator in elevator_list:
            elevator.move_to(elevator.bot_floor)


all_elevators = 0
bottom_floor = input("What is the bottom floor:")
top_floor = input("What is the top floor: ")
variables = int(input("How many elevators there are: "))
house1 = House(bottom_floor, top_floor, variables)

while all_elevators <= house1.elevators:
    all_elevators = all_elevators + 1
    elevator_list.append(Elevator(house1.bot_floor, house1.top_floor))

house1.fire_alarm()

