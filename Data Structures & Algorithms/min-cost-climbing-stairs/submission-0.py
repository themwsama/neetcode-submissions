class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])


        totalCost = [0 for i in range(len(cost) + 1)]
        totalCost[0] = cost[0]
        totalCost[1] = cost[1]
        for i in range(2, len(cost) + 1):
            totalCost[i] = min(totalCost[i-1], totalCost[i-2])
            if i != len(cost):
                totalCost[i] += cost[i]
        
        return totalCost[-1]