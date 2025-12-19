/*
 * @lc app=leetcode id=26 lang=cpp
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        //处理边界条件nums为空
        int n = nums.size();
        if (n == 0) return 0;
        //定义双指针i和j分别作为下标遍历和不重复元素的最后一个位置
        int j = 0;
        for (int i = 1; i < n; i++) {
            //条件判断，如果i不等于j，说明遇到了不重复的元素
            if (nums[i] != nums[j]) {
                //此时j继续往后挪，注意j才是第一个指针，i是第二个指针，所以j先++
                //以第一个j=0为例子，此时i=1，如果nums[1] != nums[0]，说明遇到了不重复的元素
                //此时j++，j变为1，然后将nums[1]赋值给nums[1]，即nums[j] = nums[i]
                //如果继续往后遍历，假设nums[2] == nums[1]，说明还是重复元素，此时i继续++
                //直到i=3，假设nums[3] != nums[1]，说明遇到了不重复的元素
                //此时j++，j变为2，然后将nums[3]赋值给nums[2]，即nums[j] = nums[i]
                j++;
                //一句话总结，每次遇到不重复的元素就j++，然后将当前i位置的元素赋值给j位置，构建了有效的数组
                nums[j] = nums[i];
            }
        }
        return j + 1;
    }
};
// @lc code=end

