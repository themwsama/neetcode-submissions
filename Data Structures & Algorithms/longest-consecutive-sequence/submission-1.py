class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longestSequence = 0
        countNumbers = {}

        for num in nums:
            if num in countNumbers:
                continue

            # Find left and right neighbor sets
            left_set = countNumbers.get(num - 1)
            right_set = countNumbers.get(num + 1)
            
            # Start with a set containing just the current number
            current_set = {num}

            # Merge left neighbor if it exists
            if left_set:
                current_set.update(left_set)
            
            # Merge right neighbor if it exists
            if right_set:
                current_set.update(right_set)

            # CRITICAL STEP: Update the endpoints of the new merged chain
            # The smallest number in this chain needs to point to the full set
            # The largest number in this chain needs to point to the full set
            countNumbers[min(current_set)] = current_set
            countNumbers[max(current_set)] = current_set
            
            # Also keep track of the current number itself
            countNumbers[num] = current_set
            
            longestSequence = max(longestSequence, len(current_set))

        return longestSequence
