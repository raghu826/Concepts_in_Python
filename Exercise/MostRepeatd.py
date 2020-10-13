# to find out the most repeated character in the text

text = "fbhwkajfrfbuvnifvubrs"
count = {}   # creat a dictionary
for i in text:
    if i in count:          # if char is already in the dict then increment count by 1
        count[i] += 1
    else:                   # if not make it as 1
        count[i] = 1

count_sort = sorted(count.items(), key = lambda kv :kv[1], reverse = True)

# items() func makes dict into list of tuples[()()()()]
# key is used to sort by value
# to reverse the list,  reverse = True

print(count)
print(count_sort[0])












