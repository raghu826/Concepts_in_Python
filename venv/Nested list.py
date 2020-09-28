
matrix = []
num = int(input("total no.of students: "))

if 2 <= num <= 5:
    for i in range(num):

        # Append an empty sublist inside the list
        matrix.append([])
        name  = input("Enter name: ")
        score = int(input("Enter Marks: "))
        matrix[i].append(name)
        matrix[i].append(score)
    print(matrix)

    diction = dict((set(matrix[0]),set(matrix[1])))
    print(diction)

    for i  in matrix:
        for inner in i:
            print(inner)

    new = []
    for i in matrix:
        new.append(i[1])

    new.sort()
    print(new)
    e = new[len(new)-2]
    print(e)


else:
    print("num is out of range")






