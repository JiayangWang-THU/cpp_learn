/*
 * @lc app=leetcode id=67 lang=cpp
 *
 * [67] Add Binary
 */
#include <string>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    string addBinary(string a, string b) {
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        int a_bit = 0;
        int b_bit = 0;
        string res="";
        while (i >=0 || j>=0){
            int sum = 0;
            if (i>=0){
                a_bit = int(a[i])-'0';
            }
            else{
                a_bit = 0;
            }
            if (j>=0){
                b_bit = int(b[j])-'0';
            }
            else{
                b_bit = 0;
            }
            sum = a_bit + b_bit + carry;
            carry = sum / 2;
            sum = sum % 2;
            res = to_string(sum) + res;
            i--;
            j--;
        }
        if (carry){
            res = "1" + res;
        }
        return res;
    }
};
// int main(){
//     Solution sol;
//     string a = "0";
//     string b = "0";
//     std::cout << sol.addBinary(a,b);
// }
// @lc code=end

