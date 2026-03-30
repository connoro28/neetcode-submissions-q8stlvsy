class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in numMap:
                length = 1
                while (n + length) in numMap:
                    length += 1
                longest = max(length, longest)


        return longest