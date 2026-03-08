#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
# 要实现前缀树，需要定义一个节点类
# 这个节点的两个属性，一个用于表述从当前字母node出发，下一个能走到哪些字母
# 然后如果作为一个完整的单词，我们需要知道每个node走到哪可以作为一个完整的word

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            # 帮children节点建好trienode，有点像分叉的链表
            if ch  not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node =self.root
        for ch in word:
            # 如果不在这个node的children节点里面，直接search失败
            if ch not in node.children:
                return False
            # 类似于链表继续往下走
            node = node.children[ch]
        #只有走完整个word而且还有is end才算对
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
    #search和startwith的区别就在于一个找prefix一个找完整的word
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

