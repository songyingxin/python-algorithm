#include<cstdio>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

int get_list_len(ListNode *head){
    int len = 0;
    while(head){
        head = head->next;
        len++;
    }
    return len;    
}

ListNode *move_long_list(int long_len, int short_len, ListNode *head){
    int sub = long_len - short_len;
    while(head && sub){
        head = head->next;
        sub--;
    }
    return head;
}

class Solution
{
  public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
    {
        int len_a = get_list_len(headA);
        int len_b = get_list_len(headB);

        if (len_a > len_b)
        {
            headA = move_long_list(len_a, len_b, headA);
        }
        else
        {
            headB = move_long_list(len_b, len_a, headB);
        }

        while (headA && headB)
        {
            if (headA == headB)
            {
                return headA;
            }
            headA = headA->next;
            headB = headB->next;
        }

        return nullptr;
    }
};

int main()
{
    ListNode a1(1);
    ListNode a2(2);
    ListNode b1(3);
    ListNode b2(4);
    ListNode b3(5);
    ListNode c1(6);
    ListNode c2(7);
    ListNode c3(8);
    a1.next = &a2;
    a2.next = &c1;
    c1.next = &c2;
    c2.next = &c3;
    b1.next = &b2;
    b2.next = &b3;
    b3.next = &c1;
    Solution solve;
    ListNode *result = solve.getIntersectionNode(&a1, &b1);
    printf("%d\n", result->val);
    return 0;
}
