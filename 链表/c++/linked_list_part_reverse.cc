

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
  public:
    ListNode *reverseBetween(ListNode *head, int m, int n)
    {
        int change_len = n - m + 1;  // 计算需要逆置的节点个数
        ListNode *pre_head = nullptr;  // 逆置区的前驱节点
        ListNode *result = head;  // 最终转化后的链表头节点

        while(head && --m){  // 将 head 移动m-1个位置
            pre_head = head;
            head = head->next;
        }

        ListNode *modify_list_tail = head;  // 逆置区逆置后的尾节点
        ListNode * new_head = nullptr;
        while(head && change_len){  // 逆置 change_len 个节点
            ListNode * next = head->next;
            head->next = new_head;
            new_head = head;
            head = next;
            change_len--;
        }

        modify_list_tail->next = head;
        if (pre_head){  // 说明不是从第一个节点开始逆置的
            pre_head->next = new_head;  // 将逆置链表开始的节点前驱与逆置后的头结点连接
        }
        else{
            result = new_head;   // 如果pre head为空，说明 m==1，是从第一个节点开始逆置，结果为逆置后头结点
        }

        return result;
    }
};