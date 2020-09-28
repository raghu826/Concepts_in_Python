
num = [2, 4, 3, 13, 13, 13, 13, 13, 53, 35, 1, 1, 1, 31]
newnum = sorted(num)
print(newnum)
pos = 0
item = int(input("select a number from the list: "))


def binary(newnum):
    l = 0
    u = len(newnum)-1
    global pos

    if u >= l:
        for i in range(len(newnum)):
            mid = (l + u) // 2
            if newnum[mid] == item:
                pos = mid
                return mid
            if newnum[mid] < item:
                l = mid + 1
            else:
                u = mid - 1

    else:
        return False

def find_all_occurances(newnum, item):
    index = binary(newnum)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >= 0:
        if newnum[i] == item:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i < len(newnum):
        if newnum[i] == item:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)


output = find_all_occurances(newnum, item)

print(output)

# if binary(newnum):
#     print("item found at ", pos)
# else:
#     print("not found")
