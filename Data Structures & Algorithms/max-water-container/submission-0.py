class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        left, right = 0, len(heights) - 1

        while right > left:
            maxWater = max(maxWater, min(heights[left], heights[right]) * (right - left))
            if heights[right] > heights[left]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1
                

        return maxWater