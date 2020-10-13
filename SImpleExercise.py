# Exercise is about Fizz BUZZ

def fizz_buzz(a):
    if a % 3 == 0 and a % 5 == 0:
        print("Fizz Buzz")
    elif a % 5 == 0:
        print("Buzz")
    elif a % 3 == 0:
        print("Fizz")

    return a


if __name__ == "__main__":
    print(fizz_buzz(7))
