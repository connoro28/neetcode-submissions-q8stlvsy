class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtracking(i, path, currSum):
            if currSum == target:
                res.append(path[:])
                return
            if currSum > target or i == len(candidates):
                return
            
            #all including num
            path.append(candidates[i])
            currSum += candidates[i]
            backtracking(i+1, path, currSum)
            path.pop()
            currSum -= candidates[i]
            #all not including num
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtracking(i+1, path, currSum)
        backtracking(0, [], 0)
        return res