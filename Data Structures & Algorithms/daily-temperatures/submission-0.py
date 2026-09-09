class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stackTemp = []
        result = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            if len(stackTemp) != 0:
                while (len(stackTemp) > 0) and (temperatures[i] > stackTemp[-1][1]):
                    r = stackTemp.pop()
                    result[r[0]] = i - r[0]
                    
            stackTemp.append((i, temperatures[i]))

        return result
