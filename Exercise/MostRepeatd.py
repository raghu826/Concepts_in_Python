# to find out the most repeated character in the text

text = "fbhwkajfrfbuvnifvubrs"
count = {}
for i in text:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

count_sort = sorted(count.items(), key = lambda kv :kv[1], reverse = True)

print(count)
print(count_sort[0])












