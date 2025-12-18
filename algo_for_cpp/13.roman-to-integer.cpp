/*
 * @lc app=leetcode id=13 lang=cpp
 *
 * [13] Roman to Integer
 */
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;
// @lc code=start
class Solution {
public:
    int romanToInt(string s) {
        std::unordered_map<char,int> mp ={
            {'I',1},
            {'V',5},
            {'X',10},
            {'L',50},
            {'C',100},
            {'D',500},
            {'M',1000}
        };
        int sum = 0;
        for (int i= 0; i < s.length(); ++i)
        {
            if (i+1 < s.length() && mp[s[i]] < mp[s[i+1]])
            {
                sum = sum - mp[s[i]];
            }
            else
            {
                sum = sum + mp[s[i]];
            }
        }
        return sum;
    }
};
// @lc code=end

