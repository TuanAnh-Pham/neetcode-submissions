class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carCombo = sorted(tuple(zip(position,speed)))
        fleetCount = []

        for car in carCombo:
            timeTravel = (target - car[0]) / car[1]

            while fleetCount and fleetCount[-1] <= timeTravel:
                fleetCount.pop() 

            fleetCount.append(timeTravel)

        return len(fleetCount)