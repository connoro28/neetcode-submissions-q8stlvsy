class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i, path):
            if i == len(nums):
                res.append(path[:])
                return
            #all subsets including nums[i]
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
            #all subsets not including nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1, path)
        backtrack(0, [])
        return res
