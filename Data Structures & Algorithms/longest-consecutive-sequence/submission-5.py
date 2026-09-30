class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longestSequence = 0
        seenNumbers = set(nums)

        for i in range(len(nums)):
            if (nums[i] - 1) not in seenNumbers:
                count = 0
                number = nums[i]
                while number in seenNumbers:
                    count += 1
                    number += 1
                longestSequence = max(longestSequence, count)

        return longestSequence
