def simple():
    for i in range(10):
        if (i % 2 == 0):
            yield i
            yield 2
            yield 'raghu'

        # Successive Function call using for loop


ans = simple()
print(ans.__next__())
print(ans.__next__())
print(ans.__next__())
