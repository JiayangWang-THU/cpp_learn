#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        if (n == 0) return (int)tasks.size();

        int cnt[26] = {0};
        for (char c : tasks) cnt[c - 'A']++;//统计字母个数

        int maxCount = *max_element(cnt, cnt + 26);//找最多的
        int maxCountMax = 0;
        for (int x : cnt) if (x == maxCount) maxCountMax++;//找同时为最多的

        long long frame =  (maxCount - 1) * (n + 1) + maxCountMax;//贪心公式
        return (int)max((long long)tasks.size(), frame);
    }
};
