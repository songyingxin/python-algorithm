
#include <set>

class Solution
{
  public:
    bool hasCycle(ListNode *head)
    {
        ListNode * slow = head;
        ListNode * fast = head;
        
        while(fast){
            if (fast->next == nullptr){
                return false
            }
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow){
                return true;
            }
        }
        return false
    }
};

class Solution
{
  public:
    bool hasCycle(ListNode *head)
    {
        set<ListNode *> node_set;
        while(head){
            if(node_set.find(head) != node_set.end()){
                return true;
            }
            node_set.insert(head);
            head = head->next;
        }
        return false;
    }
};