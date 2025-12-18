#include <unordered_map>
#include <cassert>
using namespace std;


 // 操作规则：
 //  get(key): 若命中，将该结点移到表头；返回其值；未命中返回 -1
 //  put(key, value):
 //     1) key 存在：更新值，并将结点移到表头
 //     2) key 不存在：在表头插入新结点；若超容量，弹出表尾结点并从哈希表删除

class LRUCache {
private:
    // 双向链表结点
    struct Node {
        int k;
        int v;
        Node* prev;
        Node* next;
        Node(int _k, int _v) : k(_k), v(_v), prev(nullptr), next(nullptr) {}
    };

    int cap;                              // 容量上限（>0）
    int sz;                               // 当前已存元素个数
    unordered_map<int, Node*> mp;         // key -> Node*
    Node* head;                           // dummy 头结点：head->next 为链表第一个有效结点(最近使用)
    Node* tail;                           // dummy 尾结点：tail->prev 为链表最后一个有效结点(最久未使用)

    // 在 head 之后插入结点 n（使其成为“最近使用”）
    void push_front(Node* n) {
        // 插入到 head 与 head->next 之间
        n->next = head->next;
        n->prev = head;
        head->next->prev = n;
        head->next = n;
    }

    // 将结点 n 从链表中移除（不 delete）
    void remove(Node* n) {
        n->prev->next = n->next;
        n->next->prev = n->prev;
        // 断开指针以避免野指针误用（可选）
        n->prev = n->next = nullptr;
    }

    // 将已有结点 n 移动到表头（最近使用）
    void move_to_front(Node* n) {
        remove(n);
        push_front(n);
    }

    // 弹出表尾的“有效结点”（即 tail->prev），并返回其指针（调用方负责 delete）
    Node* pop_back() {
        Node* n = tail->prev;
        if (n == head) return nullptr; // 空链表，无有效结点
        remove(n);
        return n;
    }

public:
    // 构造：初始化容量并创建 dummy 头尾
    explicit LRUCache(int capacity) : cap(capacity), sz(0) {
        assert(capacity > 0 && "LRU capacity must be > 0");
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head->next = tail;
        tail->prev = head;
    }

    // 析构：释放所有结点（包含 dummy）
    ~LRUCache() {
        Node* cur = head;
        while (cur) {
            Node* nxt = cur->next;
            delete cur;
            cur = nxt;
        }
    }

    // O(1) 查询：命中则移到表头并返回值；未命中返回 -1
    int get(int key) {
        auto it = mp.find(key);
        if (it == mp.end()) {
            return -1; // 未命中
        }
        Node* n = it->second;
        move_to_front(n); // 最近使用
        return n->v;
    }

    // O(1) 更新/插入：必要时淘汰最久未使用
    void put(int key, int value) {
        auto it = mp.find(key);
        if (it != mp.end()) {
            // 已存在：更新值并提升为最近使用
            Node* n = it->second;
            n->v = value;
            move_to_front(n);
            return;
        }

        // 不存在：创建新结点，插入表头，并写入哈希表
        Node* n = new Node(key, value);
        mp[key] = n;
        push_front(n);
        ++sz;

        // 若超出容量：弹出表尾有效结点并清理哈希表/内存
        if (sz > cap) {
            Node* victim = pop_back();        // 最久未使用
            mp.erase(victim->k);              // 从哈希表移除
            delete victim;                    // 释放内存
            --sz;
        }
    }
};


