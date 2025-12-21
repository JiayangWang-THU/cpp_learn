#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def add_digits(A, B):
            i = len(A) - 1
            j = len(B) - 1
            carry = 0
            res = []

            while i >= 0 or j >= 0:
                a = A[i] if i >= 0 else 0 #这里是py的三元条件true if con else false）
                b = B[j] if j >= 0 else 0

                s = a + b + carry
                res.append(s % 10) #取余数
                carry = s // 10 #取整数

                i -= 1
                j -= 1

            if carry:
                res.append(carry)

            return res[::-1] #反转列表
        return add_digits(digits, [1])  
# @lc code=end

