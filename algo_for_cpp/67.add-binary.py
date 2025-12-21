#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []
        n1 = len(a)-1
        n2 = len(b)-1
        while n1 >= 0 or n2 >= 0 :
            a_bit = int(a[n1]) if n1 >= 0 else 0
            b_bit = int(b[n2]) if n2 >= 0 else 0
            s = a_bit + b_bit + carry
            res.append(str(s % 2))
            carry = s // 2
            n1 -= 1
            n2 -= 1
        if carry:
            res.append(str(carry))
        return ''.join(res[::-1])
# @lc code=end

def main():
    sol = Solution()
    a = "11"
    b = "1"
    print(sol.addBinary(a, b))
if __name__ == "__main__":
    main()