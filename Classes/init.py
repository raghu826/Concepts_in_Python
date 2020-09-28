class Car:

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def specs(self):
        print("features of the car:", self.name, self.cost )


bmw = Car('BMW', '10c')

bmw.specs()