def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    res = []
    dict = {}

    for i in range(len(nums)):
        dict[nums[i]] = i
    for i in range(len(nums)):
        temp = target - nums[i]
        if dict.get(temp) and dict.get(temp) != i:
            res.append(i)
            res.append(dict.get(temp))
            break
    return res


nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))