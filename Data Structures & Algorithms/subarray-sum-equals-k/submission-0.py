class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        mp = {0:1}
        prefixSum = 0
        for n in nums:
            prefixSum += n
            if prefixSum - k in mp:
                res += mp[prefixSum - k]
            mp[prefixSum] = mp.get(prefixSum, 0) + 1

        return res

