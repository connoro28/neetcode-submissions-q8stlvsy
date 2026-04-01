class Solution:
    from collections import defaultdict
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #creating a map to map every course to an empty list
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        
        #adds prerequisit to the map
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            #if there is a loop
            if crs in visited:
                return False
            #if there is no prereqs to a course
            if preMap[crs] == []:
                return True
            #first add the current course to the visited set
            visited.add(crs)
            # if preReq is not 
            for pre in preMap[crs]:
                if not dfs(pre) : return False
            visited.remove(crs)
            #replaces the dict with an empty list to show that prereq sequence works
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


        
