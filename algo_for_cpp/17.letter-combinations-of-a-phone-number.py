#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        path = []

        def backtrack(index):
            # 走到末尾，说明形成一个完整组合
            if index == len(digits):
                res.append("".join(path))
                return

            # 当前这一位数字能对应哪些字母
            letters = phone[digits[index]]

            for ch in letters:
                path.append(ch)
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return res
# @lc code=end

