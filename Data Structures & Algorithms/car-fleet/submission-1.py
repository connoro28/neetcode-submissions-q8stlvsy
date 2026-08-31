class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = [[p,s] for p, s in zip(position, speed)]
        fleets = 0
        slowest = 0.0
        for p, s in sorted(pairs)[::-1]:
            time = float((target - p) / s)
            if time > slowest:
                fleets += 1
                slowest = time
        return fleets
            

