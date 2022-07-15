# Objects
class PartyAnimal:
    x = 0

    def __init__(self, name):
        self.name = name
        print(self.name,' constructed')

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


an = PartyAnimal()
an.party()
an.party()
an = 42
print(an)

# Inheritance
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print('My points', self.points)

jim = FootballFan("Jim")
jim.party()
jim.touchdown()