import heapq
class MedianFinder:

    def __init__(self):
        #create a small and a large side heaps, one is max heap on left and one is min heap
        self.small = []
        self.large = []
    def addNum(self, num: int) -> None:
        # add all new numbers to the small max heap
        heapq.heappush(self.small, -num)
        #if the top of the small numbers is bigger than the bottom of the larger move that one over to the large
        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        #rebalance, if smalllen > largelen + 1 move small top to large bottom
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        #same but swithced largelen > smalllen + 1
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))
    def findMedian(self) -> float:
        #if one length is odd than take that
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        elif len(self.large) > len(self.small):
            return float(self.large[0])
        else:
            return ((-self.small[0]) + (self.large[0])) / 2.0

        #if both even then peek top of both and float divide
        