class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numOccurences = {}
        for n in nums:
            numOccurences[n] = 1 + numOccurences.get(n, 0) 
        
        freqElements = [[] for i in range(len(nums) + 1)]

        for number, occurences in numOccurences.items():
            freqElements[occurences].append(number)

        output = []

        index = len(freqElements)-1
        while k > 0:
            if len(freqElements[index]) == 0:
                index -= 1
                continue
            if index < 0:
                break
            removedItem = freqElements[index].pop()
            output.append(removedItem)
            k -= 1

        return output