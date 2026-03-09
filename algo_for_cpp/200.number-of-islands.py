#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 岛屿数量，我的第一想法是找到类似于一个点为1，周围4个点都为0的结构
        # 岛的大小也是不确定的，所以肯定是要先把岛屿的外轮廓形状求出来
        # 但是正所谓正难则反
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(i, j):
            # 1. 越界
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return

            # 2. 不是陆地，直接停
            if grid[i][j] != '1':
                return

            # 3. 标记当前格子已经访问过
            grid[i][j] = '0'

            # 4. 向四个方向扩散
            dfs(i - 1, j)   # 上
            dfs(i + 1, j)   # 下
            dfs(i, j - 1)   # 左
            dfs(i, j + 1)   # 右

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count
# @lc code=end

