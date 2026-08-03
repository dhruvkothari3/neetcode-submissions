class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for p, s in zip(position, speed):
            time = (target - p) / s
            cars.append([p, time])

        cars.sort(reverse=True)

        fleets = 0
        previous_time = 0

        for p, time in cars:
            if time > previous_time:
                fleets += 1
                previous_time = time

        return fleets