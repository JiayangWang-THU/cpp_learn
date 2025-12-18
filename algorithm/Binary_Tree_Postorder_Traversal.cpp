/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;                // 用来装最终后序序列
        if (!root) return res;          // 空树：直接返回空结果

        stack<TreeNode*> st1, st2;      // st1 负责处理顺序，st2 负责倒序收集
        st1.push(root);                 // 先把根压入 st1，作为入口

        while (!st1.empty()) {          // 只要 st1 还有待处理节点
            TreeNode* node = st1.top(); // 取出栈顶（注意：此处必须先声明 TreeNode* node）
            st1.pop();                  // 弹出它，表示“当前要处理”
            st2.push(node);             // 把它压到 st2：形成“根→右→左”的序列雏形

            // 这里的压栈顺序很关键：
            // 我们“先压左，再压右”，因为 st1 是栈（后进先出），
            // 这样下一轮会“先处理右，再处理左”，从而在 st2 中形成“根→右→左”的顺序。
            // 最终把 st2 逆序弹出，就得到“左→右→根”的后序遍历。
            if (node->left)  st1.push(node->left);   // 先压左
            if (node->right) st1.push(node->right);  // 后压右
        }

        // 此时 st2 内部的顺序是：Root, Right, Left（按“处理时刻”的逆序堆叠出来）
        // 逆序弹出 st2，得到 Left, Right, Root —— 正是后序遍历
        while (!st2.empty()) {
            res.push_back(st2.top()->val);
            st2.pop();
        }
        return res;
    }
};
