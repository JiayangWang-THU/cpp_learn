/*
 * @lc app=leetcode id=268 lang=cpp
 *
 * [268] Missing Number
 */

// @lc code=start
class Solution {
public:
    int missingNumber(vector<int>& nums) {
       
    }
};
// @lc code=end


//排序方法
//  sort(nums.begin(),nums.end());
//         for (int i=0;i<nums.size();i++){
//             if(nums[i]!=i)
//                 return i;
//         }
//         return nums.size();
//

//数学方法
// int n = nums.size();
//        int  sum = n*(n+1)/2;
//        int num_sum = accumulate(nums.begin(), nums.end(), 0);
//        return sum - num_sum;