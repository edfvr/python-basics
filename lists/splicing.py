nums = [1, 2, 3, 4]
print("before: ")
print(nums)

nums[len(nums):] = [5]
print("after: ")
print(nums)