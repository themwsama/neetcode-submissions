class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        items = {}

        for i in range(0,len(nums)):
            items[nums[i]] = i
       
        for i in range(0,len(nums)):
            if ((target - nums[i]) in items) and (i != items[target - nums[i]]):
                return [i, items[target - nums[i]]]

        return [0,0]
        