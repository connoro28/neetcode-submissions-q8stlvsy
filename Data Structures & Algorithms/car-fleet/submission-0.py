class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timeStack = []
        pairs = [[p,s] for p, s in zip(position, speed)]

        for p, s in sorted(pairs)[::-1]:
            time = float((target - p) / s)
            if timeStack:
                if timeStack[-1] >= time:
                    continue
                else:
                    timeStack.append(time)
            else:
                timeStack.append(time)
        return len(timeStack)
            

