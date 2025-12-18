class Solution {
public:
    void dfs(vector<vector<char>>& grid, int r, int c) {
        int R = grid.size(), C = grid[0].size();
        //  越界或不是陆地就返回
        if (r < 0 || r >= R || c < 0 || c >= C || grid[r][c] != '1') return;

        //  标记访问（淹掉当前格子）
        grid[r][c] = '0';

        //  四个方向继续扩散
        dfs(grid, r - 1, c); // 上
        dfs(grid, r + 1, c); // 下
        dfs(grid, r, c - 1); // 左
        dfs(grid, r, c + 1); // 右
    }

    int numIslands(vector<vector<char>>& grid) {
        int R = grid.size();
        if (R == 0) return 0;
        int C = grid[0].size();

        int count = 0;
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                // 每发现一个新的陆地块，计数 +1，然后淹没它
                if (grid[r][c] == '1') {
                    ++count;
                    dfs(grid, r, c);
                }
            }
        }
        return count;
    }
};
