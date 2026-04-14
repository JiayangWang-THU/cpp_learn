
nums = [64, 34, 25, 12, 22, 11, 90]
def bubble_sort(nums):
    n = len(nums)
    # i记录已经有多少个大泡泡升到了顶端
    for i in range(n):
        # 用于提前结束冒泡，避免对已经有序的数组继续遍历比较
        swapped = False
        # j 是活动范围，范围是0到n-i-1
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums
print(bubble_sort(nums))