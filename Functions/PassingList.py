#Function to return the string with more Than five letters
names = []   # Empty list

total = int(input("Total no.of names:"))  

for i in range(total):          # adding names to the list
    a = input("Enter next name:")
    names.append(a)

print(names)


def bigname(names):

    count = 0
    for e in names:         # traversing through the list
        if len(e) > 5:
            count += 1
            print(e)

    print("Number of names with more than five letters:", count )
    return e, count


info = bigname(names)

