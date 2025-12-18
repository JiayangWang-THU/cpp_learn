class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());//升序排序，排完序之后什么都好说了
        int n = nums.size();
        int ans = 0;
        for (int k = n - 1; k >= 2; --k) {
            int i = 0, j = k - 1;
            while (i < j) {
                if (nums[i] + nums[j] > nums[k]) {//较小的边相加要大于较大的边
                    ans += (j - i);
                    --j;
                } else {
                    ++i;
                }
            }
        }
        return ans;
    }
};