class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) return head;

        // 情况1：反转从头结点开始
        if (left == 1) {
            ListNode* prev = nullptr;
            ListNode* curr = head;
            for (int i = 0; i < right; i++) {
                ListNode* next = curr->next;
                curr->next = prev;
                prev = curr;
                curr = next;
            }
            head->next = curr; // 原来的头节点成了尾巴
            return prev;       // prev 成为新的头节点
        }

        // 情况2：反转不是从头开始
        ListNode* pre = head;
        for (int i = 1; i < left - 1; i++) {
            pre = pre->next;
        }

        ListNode* curr = pre->next;
        ListNode* prev = nullptr;
        for (int i = 0; i <= right - left; i++) {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }

        pre->next->next = curr; // 接上后半段
        pre->next = prev;       // 接上反转后的头

        return head;
    }
};
