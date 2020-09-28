
lst = [3, 5, 8, 4, 9]

n = 9
pos = 0

def search():
    global pos
    for i in lst:
        if i == n:
            print("Found at index", pos)
        pos = pos + 1
    return True


if search():
    print("number exist in list")
else:
    print("not found")