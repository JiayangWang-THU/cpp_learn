/*
 * @lc app=leetcode id=118 lang=cpp
 *
 * [118] Pascal's Triangle
 */
#include <vector>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res;
        vector<int> row_last={1,1};
        vector<int> row_now;
        if (numRows == 1){
            res.push_back({1});
            return res;
        }
        if (numRows == 2){
            res.push_back({1});
            res.push_back({1,1});
            return res;
        }
        if (numRows >=3){
            for (int i=0;i<numRows;i++){
                row_now.clear();
                for (int j=0;j<=i;j++){
                    if (j==0 || j==i){
                        row_now.push_back(1);
                                    }
                    else{
                        row_now.push_back(row_last[j]+row_last[j-1]);
                    }
                
                    }
                row_last = row_now;
                res.push_back(row_now);
                }
            return res;

            }
        }
    
};
// @lc code=end

