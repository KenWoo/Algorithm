def twoSum(nums, target):
    # Time Limit Exceeded
    # for i in range(len(nums) - 1):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    dict = {}
    for i in range(len(nums)):
        if target - nums[i] in dict:
            return [dict[target - nums[i]], i]
        else:
            dict[nums[i]] = i


print(twoSum([3, 2, 4], 6))
