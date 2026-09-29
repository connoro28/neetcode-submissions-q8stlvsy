class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0
        while l <= r:
            k = (r+l)// 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p)/k)
            if hours <= h:
                res = k
                r = k - 1
            elif hours > h:
                l = k + 1
        return res