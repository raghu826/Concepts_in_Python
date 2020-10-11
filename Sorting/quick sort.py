# implementing quick sort

def quick_sort(nums):
    length = len(nums)
    if length <= 1:
        return nums

    pivot = nums[length//2] # insert any index as pivot
    small_nums = []
    large_nums = []
    middle = []  # list sorted in first iteration

    for i in nums:
        if i > pivot:
            large_nums.append(i)
        elif i == pivot:
            middle.append(i)
        else:
            small_nums.append(i)

    return quick_sort(small_nums) + middle + quick_sort(large_nums)


if __name__ == '__main__':
    item = [
        [2, 2, 4,2,3,45,7],
        [1,2,3,4,5,6],
        [9,8,7,6,5,4],
        [],
        [3,3,3,3,3]
        ]
    for i in item:
        print(quick_sort(i))
