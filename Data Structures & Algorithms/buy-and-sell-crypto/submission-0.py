class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        left, right, maxprofit = 0, 1, 0

        while right < len(prices) and left < len(prices):
            maxprofit = max(maxprofit, prices[right] - prices[left])
            
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                right += 1


        return maxprofit