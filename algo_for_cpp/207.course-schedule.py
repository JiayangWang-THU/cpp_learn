#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        visited = [0] * numCourses   # 0=未访问, 1=访问中, 2=已完成

        def dfs(course):
            if visited[course] == 1:
                return False   # 发现环
            if visited[course] == 2:
                return True    # 之前已经检查过，没问题

            visited[course] = 1  # 标记为访问中

            for nxt in graph[course]:
                if not dfs(nxt):
                    return False

            visited[course] = 2  # 标记为已完成
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
# @lc code=end

