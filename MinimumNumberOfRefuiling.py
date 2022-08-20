import heapq  # for pop min
#we use negative nums in heap to pop the -biggest every time

class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: list[list[int]]
    ) -> int:

        stations.append([target, 0])

        previous, count = 0, 0
        fuel = startFuel
        missed_fuel = []

        for position, station_fuel in stations:
            distance = position - previous
            previous = position

            if fuel < distance:

                while missed_fuel and fuel < distance:
                    fuel += -heapq.heappop(missed_fuel)
                    count += 1

                if fuel < distance:
                    return -1

            fuel -= distance
            heapq.heappush(missed_fuel, -station_fuel)

        return count
