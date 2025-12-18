#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = INT_MAX;
        int maxProfit = 0;
        for (int p : prices) {
            minPrice = min(minPrice, p);           // 更新最低买入价
            maxProfit = max(maxProfit, p - minPrice); // 更新最大利润
        }
        return maxProfit;
    }
};
