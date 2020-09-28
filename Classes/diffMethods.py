class Student:
    university = 'Bauhaus'

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def info(self):
        print("details", self.name, self.roll, self.university)
        
    @classmethod
    def uniName(cls):
        print(cls.university)


s1 = Student('meeee',125)

s1.info()
Student.uniName()


