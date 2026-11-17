import copy

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        n cars

        position [int] length n

        speed [int] length n

        destination is 'target'

        """
        number_fleets = 0
        cars = sorted(zip(position, speed), reverse=True)
        prev_time = 0

        for pos, sped in cars:
            time = (target - pos)/sped
                
            # if the time to get to target longer than car ahead, it will never catchup, so new fleet
            if time > prev_time:
                number_fleets += 1
                prev_time = time


        return number_fleets