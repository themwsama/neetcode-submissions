class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        listtriplets = []
        n = len(nums)
        
        for i in range(n):
            # Skip duplicate elements for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            leftpt = i + 1
            rightpt = n - 1
            
            while leftpt < rightpt:
                current_sum = nums[i] + nums[leftpt] + nums[rightpt]
                
                if current_sum < 0:
                    leftpt += 1
                elif current_sum > 0:
                    rightpt -= 1
                else:
                    listtriplets.append([nums[i], nums[leftpt], nums[rightpt]])
                    
                    # Skip duplicate elements for leftpt and rightpt
                    while leftpt < rightpt and nums[leftpt] == nums[leftpt + 1]:
                        leftpt += 1
                    while leftpt < rightpt and nums[rightpt] == nums[rightpt - 1]:
                        rightpt -= 1
                        
                    leftpt += 1
                    rightpt -= 1
                    
        return listtriplets
