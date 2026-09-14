class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # visitSet = all courses along the curr DFS path
        visitSet = set()
        def dfs(crs):
            # If crs in visitSet, we've detected a cycle and can't complete
            # all courses
            if crs in visitSet:
                return False
            # If prereq list is empty, we are good to complete this crs
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = [] # Completed all prereqs for this crs
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True