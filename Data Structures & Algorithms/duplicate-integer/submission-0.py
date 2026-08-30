class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number = {}
        for n in nums:
            if n in number:
                return True
            number[n] = True
        return False
        