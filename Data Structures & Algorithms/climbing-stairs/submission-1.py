class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0 for i in range(n)]


        for i in range(n):
            if i == 0:
                steps[0] = 1
            elif i == 1:
                steps[i] = 2
            else:
                steps[i] = steps[i-2] + steps[i-1]
                
            
        return steps[-1]