class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = (int)nums.size();
        int maxReach = 0;                 // 目前能到达的最远下标
        for (int i = 0; i < n; ++i) {
            if (i > maxReach) return false;                  // 到不了当前位置
            maxReach = max(maxReach, i + nums[i]);           // 扩张可达范围
            if (maxReach >= n - 1) return true;              // 已能到终点
        }
        return true; // 遍历完
    }
};
