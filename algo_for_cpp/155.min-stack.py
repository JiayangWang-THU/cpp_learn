#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:
    # 最小栈的题
    # 建一个栈，而且能快速找到最小值
    # 栈本身一般在python里面是拿列表建的
    # 这里相当于维护两个栈，一个是正常栈，另一个是附属于正常栈的最小栈
    # 能保证存住历史信息，一般常数项的时间复杂度基本上都是直接取用得到的
    #
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            # 最小也具有传递性，如果你不能比当前的min小，那就直接复制刚才的min
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

