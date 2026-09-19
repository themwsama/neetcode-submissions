class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        leftSpeed, rightSpeed = 1, max(piles) 
        slowestSpeed = max(piles)

        while leftSpeed <= rightSpeed:
            spd = (rightSpeed + leftSpeed) // 2
            hours = 0
          
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / spd)
                if hours > h:
                    break

            if hours <= h:
                slowestSpeed = min(slowestSpeed, spd)
                rightSpeed = (rightSpeed + leftSpeed) // 2 - 1
            else:
                leftSpeed = (rightSpeed + leftSpeed) // 2 + 1
                
            
        return slowestSpeed