class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist = {}
        for n in nums:
            if n in exist:
                return True
            exist[n] = True
        return False
        