class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lft, rht, maxarea = 0, len(heights)-1, 0

        while (rht > lft):
            area = (rht - lft) * min(heights[lft], heights[rht])
            maxarea = max(maxarea, area)

            if (heights[lft] > heights[rht]):
                rht -= 1
            else:
                lft += 1

        return maxarea