# https://leetcode.com/problems/car-fleet/submissions/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # The car that has the shortest distance to target is first.
        sorted_cars =  sorted(zip(position, speed), reverse=True)
        if len(sorted_cars) == 1:
            return 1
        
        car_fleets = 0
        current_fleet_time = 0
        for p, s in sorted_cars:
            current_car_time = (target - p) / s
            # Any car that has a greater time than the max time will inherently join a new fleet.
            # E.g., if car has a higher reach time than the current fleet, that car will never 
            # reach the fleet. So increment the number of fleets and change the fleet time to the time of the current car.
            if current_car_time > current_fleet_time:
                current_fleet_time = current_car_time
                car_fleets += 1

        return car_fleets
