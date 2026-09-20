class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        purchase_index = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - prices[purchase_index])
            purchase_index = i if prices[i] < prices[purchase_index] else purchase_index

        return profit