
class Handle:

    def handling(self):

        try:
            a = int(input("Enter number"))
            b = int(input("Enter number"))
            c = a / b
            print(c)

        except Exception as e:

            print(r" denominator should not be zero" , e)
        else:
            print("if exception fails else will execute ")

        finally:
            print("egal")  # it executes whatever happens


H = Handle()
H.handling()

