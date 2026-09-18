class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while right >= left:
            middle = (right+left)//2 
            if target == nums[middle]:
                return middle
            elif nums[middle] > target:
                right = middle-1
            else:
        
                left = middle +1

        return -1