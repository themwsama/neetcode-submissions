class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        array = [0 for i in range(len(temperatures))]
        stackOfTemp = []
        for i in range (len(temperatures)):
            while stackOfTemp and temperatures[stackOfTemp[-1]] < temperatures[i]:
                index = stackOfTemp.pop()
                array[index] = i - index
            stackOfTemp.append(i)
        return array

        