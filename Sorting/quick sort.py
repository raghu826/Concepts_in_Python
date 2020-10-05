# implementing quick sort
# executed only using pop function

def quick_sort(nums):
    length = len(nums)
    if length <= 1:
        return nums
    else:
        pivot = nums.pop()

    small_nums = []
    large_nums = []

    for i in nums:
        if i > pivot:
            large_nums.append(i)
        else:
            small_nums.append(i)

    return quick_sort(small_nums) + [pivot] + quick_sort(large_nums)


if __name__ == '__main__':
    item = [7, 3, 6, 2, 8, 3, 9, 2, 5, 1, 5]
    print(quick_sort(item))
