# implementing bubble sort

lst = []

num = int(input("length of the list: " ))

for i in range(num):
    p = input("enter list item: ")
    lst.append(p)

print(lst)


def sort(lst):
    for j in range(len(lst)-2):
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1], lst[i]
    print(lst)

sort(lst)