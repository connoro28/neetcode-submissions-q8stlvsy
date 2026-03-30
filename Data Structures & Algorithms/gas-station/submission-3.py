class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = 0
        l = 0
        tSum = 0
        maxDiff = 0
        for n in range(len(gas)):
            diff = diff + gas[n] - cost[n]
        if diff < 0:
            return -1
        diff = 0
        for n in range(len(gas)):
            diff = gas[n] - cost[n]
            tSum = tSum + diff
            if tSum < 0:
                tSum = 0
                l = n+1
        return l

        