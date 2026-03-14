#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 括号生成的问题
        # 生成所有的括号可能
        # 首先我们要分析的是括号本身的规则
        # 要么并列关系要么嵌套关系
        # 一个括号的时候没什么好说的就是正常的括号
        # 叠加了一个括号就多了两种可能，并列和嵌套
        # 再叠加一个括号就是，要前面两个可能的救出上每个再多两个可能
        # 所以这有点类似于一个二叉树了，每次在这个分支上会多两种可能
        if n == 0:
            return []

        dp = [set() for _ in range(n + 1)]
        dp[1].add("()")

        for i in range(2, n + 1):
            for s in dp[i - 1]:
                for pos in range(len(s) + 1):
                    new_s = s[:pos] + "()" + s[pos:]
                    dp[i].add(new_s)

        return list(dp[n])
# @lc code=end

