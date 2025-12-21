/*
 * @lc app=leetcode id=66 lang=cpp
 *
 * [66] Plus One
 */

// @lc code=start
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 1;
        int n = digits.size();
        for (int i = n - 1;i>=0;i--){
            int s;
            s = digits[i] + carry;
            digits[i] = s % 10;
            carry = s / 10;
            if (i == 0 && carry==1){
                digits.insert(digits.begin(),1);
                return digits;
            }
            if (carry == 0){
                return digits;
            }
        }
        return digits;
    }
};
// @lc code=end

