"""
Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin
ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen

"""


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


h1 = Elevator(1, 5)

h1.move_to(4)
h1.move_to(h1.bot_floor)
h1.one_up()
h1.one_down()
h1.one_down()
h1.move_to(h1.top_floor)
h1.one_up()
h1.move_to(h1.bot_floor)


