class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        l = 0
        r = l+1
        total = 0
        for l in range(len(gas)):
            if l != len(gas)-1:
                r = l+1
            else:
                r = 0
            total = gas[l] - cost[l]
            while total >= 0 and r!=l:
                total = total + gas[r] - cost[r]
                if r == len(gas)-1:
                    r = 0
                else:
                    r+=1
            if r == l:
                return l
