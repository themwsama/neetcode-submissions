class Solution:
    def climbStairs(self, n: int) -> int:
        if n<= 2:
            return n
        steps = [0 for i in range(n)]
        steps[0] = 1
        steps[1] = 2
        for i in range(2,n):
            steps[i] = steps[i-2] + steps[i-1]
        return steps[-1]