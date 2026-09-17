class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        answer = [-1, -1]

        for i in range(len(nums)):
            numbers[nums[i]] = i

        for i in range(len(nums)):
            if (target - nums[i]) in numbers and i != numbers[target-nums[i]]:
                answer = [i, numbers[target-nums[i]]]
                answer.sort()
                break

        return answer