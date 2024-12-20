def majority_element(nums):
    nums.sort()
    return nums[len(nums) // 2]

nums = [3, 3, 4, 2, 2, 2, 2, 2, 2, 3, 3, 3]
print(majority_element(nums)) 
