#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 这题相当于我们已知一些
        # 基本的变量之间的除法关系
        # 我们要得到其他的除法结果，如果没见过就返回-1
        graph = defaultdict(list)

        # 建图
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1 / v))

        def dfs(cur, target, visited):
            # 变量不存在
            if cur not in graph or target not in graph:
                return -1.0

            # 找到目标
            if cur == target:
                return 1.0

            visited.add(cur)

            for nxt, weight in graph[cur]:
                if nxt in visited:
                    continue

                sub = dfs(nxt, target, visited)
                if sub != -1.0:
                    return weight * sub

            return -1.0

        ans = []
        for a, b in queries:
            ans.append(dfs(a, b, set()))

        return ans
# @lc code=end

