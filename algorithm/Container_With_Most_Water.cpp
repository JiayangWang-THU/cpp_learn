#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0, r = (int)height.size() - 1;
        int ans = 0;
        while (l < r) {
            // 当前容器的高度由短板决定
            int h = min(height[l], height[r]);
            // 当前宽度是 r - l
            ans = max(ans, h * (r - l));

            // 只移动短板一侧，才可能让高度上限变大
            if (height[l] < height[r]) {
                ++l;
            } else {
                --r;
            }
        }
        return ans;
    }
};
