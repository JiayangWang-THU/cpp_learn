#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> ans(n, 0);
        stack<int> st; // 栈中存的是下标，对应的温度是递减的

        // 从左到右遍历每一天
        for (int i = 0; i < n; ++i) {
            int currentTemp = temperatures[i];

            // 当遇到比栈顶温度更高的天
            // 就说明栈顶那天等到了更热的一天
            while (!st.empty() && currentTemp > temperatures[st.top()]) {
                int prevIndex = st.top(); // 弹出那天的下标
                st.pop();
                ans[prevIndex] = i - prevIndex; // 计算间隔天数
            }

            // 当前天入栈，等待未来更热的一天
            st.push(i);
        }

        return ans;
    }
};
