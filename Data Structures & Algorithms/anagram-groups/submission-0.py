class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultMap = defaultdict(list)
        for string in strs:
            countList = [0]*26
            for char in string:
                index = ord(char)-ord("a")
                countList[index]+=1
            resultMap[tuple(countList)].append(string)
        return list(resultMap.values())