import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            distance = x*x + y*y
            heapq.heappush(heap,(distance,x,y))
        for _ in range(k):
            d, x, y = heapq.heappop(heap)
            res.append([x,y])
        return res

        
