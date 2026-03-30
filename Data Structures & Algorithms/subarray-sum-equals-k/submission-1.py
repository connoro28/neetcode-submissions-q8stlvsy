class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        sumMap = {0:1}
        count = 0
        for n in nums:
            prefixSum = prefixSum + n
            if prefixSum - k in sumMap:
                count+=sumMap[prefixSum-k]
                sumMap[prefixSum] = sumMap.get(prefixSum, 0) + 1
            else:
                sumMap[prefixSum] = sumMap.get(prefixSum, 0) + 1
        return count
            
