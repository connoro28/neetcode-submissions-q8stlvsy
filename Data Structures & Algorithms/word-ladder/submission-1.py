from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                patterns[word[:i] + "*" + word[i+1:]].append(word)
        q = deque()
        q.append(beginWord)
        visited = set()
        count = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for i in range(len(word)):
                    for nei in patterns[word[:i] + "*" + word[i+1:]]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            count+=1
        return 0
        



        
