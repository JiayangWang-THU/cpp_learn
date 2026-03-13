#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        def funct(k,str):
            return k*str
        # 我感觉这个顺序应该是从里往外
        # 问题就在于怎么得到s的从里往外
        # 有点像括号抵消的思路
        # 用栈来存
        # 碰到第一个消去左右括号的位置就是最里面
        stack = []
        cur_num = 0
        cur_str = ""

        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)

            elif ch == '[':
                # 保存进入这一层之前的状态
                stack.append((cur_str, cur_num))
                cur_str = ""
                cur_num = 0

            elif ch == ']':
                # 当前层结束，弹出上一层状态
                prev_str, num = stack.pop()
                cur_str = prev_str + funct(num,cur_str)

            else:
                # 普通字母
                cur_str += ch

        return cur_str
# @lc code=end

