class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;           // 存放结果
        stack<TreeNode*> st;       // 模拟递归调用栈
        TreeNode* cur = root;      // 游标，从根开始

        // 只要当前节点还存在，或者栈里还有待处理的结点，就继续循环
        while (cur || !st.empty()) {
            
            // 一路向左，把沿途所有节点先压栈
            // 模拟递归调用：inorder(node->left)
            while (cur) {
                st.push(cur);      // 先记录当前节点，等左子树处理完再回来
                cur = cur->left;  // 指针转向左子树
            }

            // 走到最左后，cur 已经是 nullptr
            // 开始回溯：取出栈顶，就是当前要访问的节点
            cur = st.top();       
            st.pop();

            // 访问这个节点（根）
            res.push_back(cur->val);

            //  转向右子树
            //  模拟递归调用：inorder(node->right)
            cur = cur->right;
        }

        return res;
    }
};
