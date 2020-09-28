class Person:

    # def __init__(self,height, weight):
    #     self.height = height
    #     self.weight = weight

    def eat(self, height, weight):
        print(self.height,  self.weight)

    def update_eat(self, func):
        def inner(height, weight):
            return self.func((height + weight)/2)
        return inner


p = Person()

eat1 = p.update_eat.eat
eat1(20,20)



