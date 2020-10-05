# implementing bubble sort

lst = []

num = int(input("length of the list: " ))

for i in range(num):
    p = input("enter list item: ")
    lst.append(p)
print(lst)


def sort(lst):
    for i in range(len(lst)-2):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
    print(lst)

sort(lst)

# applying bubble sort for a list contain dictionaries
def bubble_sort(elements, key = None):

    for i in range(len(elements) - 2):
        for j in range(len(elements) - 1-i): #here -i indicates no.of sorted elements
            if elements[j][key] > elements[j+1][key]:
                elements[j][key], elements[j+1][key] = elements[j+1][key], elements[j][key]

    print(elements)


if __name__ == "__main__":
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'}   ]

    bubble_sort(elements, key='device')
    bubble_sort(elements, key='name')
    bubble_sort(elements, key='transaction_amount')
