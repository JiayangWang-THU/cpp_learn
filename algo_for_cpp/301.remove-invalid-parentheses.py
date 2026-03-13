#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 感觉和valid parentheses反着来
        # 原来只是括号消消乐
        # 一般用栈的性质就可以解决了
        # 我想的是穷举删哪些
        # 然后用valid括号来验证
        # 但是搜索空间就是
        # 如果s长度为n
        # 每个位置都有删或者不删的选项
        # 这样就是二的指数级数的增长速度了
        # 这样肯定会TLE
        def is_valid(string: str) -> bool:
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        res = []
        visited = set([s])
        queue = deque([s])
        found = False
        '''
        1 原字符串入队
        2 BFS层序遍历
        3 每一层表示删除次数
        4 一旦某层出现合法字符串
        5 收集所有合法字符串
        6 停止搜索
        '''
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                cur = queue.popleft()

                # 先检查当前层有没有合法答案
                if is_valid(cur):
                    res.append(cur)
                    found = True

                # 如果这一层已经找到合法答案
                # 就不要再生成下一层了
                if found:
                    continue

                # 枚举删除一个括号的位置
                for i in range(len(cur)):
                    if cur[i] not in '()':
                        continue

                    nxt = cur[:i] + cur[i+1:]

                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)

            # 这一层找到后，直接停
            if found:
                break

        return res
# @lc code=end

