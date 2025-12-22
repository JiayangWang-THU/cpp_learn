/*
 * @lc app=leetcode id=119 lang=cpp
 *
 * [119] Pascal's Triangle II
 */

// @lc code=start
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector <int> row_last={1,1};
        vector <int> row_now;
        if (rowIndex == 0){
            return {1};
        }
        if (rowIndex ==1){
            return {1,1};
        }
        if (rowIndex >= 2){
            for (int i=2;i<=rowIndex;i++){
                row_now.clear();
                for (int j=0;j<=i;j++){
                    if(j==0 || j == i){
                        row_now.push_back(1);
                    }
                    else{
                        row_now.push_back(row_last[j-1]+row_last[j]);
                    }
                    }
                row_last = row_now;
                }
            return row_now;
            }
            return {};
        }
    };
// @lc code=end

