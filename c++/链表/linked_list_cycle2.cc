class Solution
{
  public:
    ListNode *detectCycle(ListNode *head)
    {
        ListNode *slow = head;
        ListNode *fast = head;
        bool is_meet = false;

        while (fast)
        {
            if (fast->next == nullptr)
            {
                return nullptr;
            }
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow)
            {
                is_meet = true;
                break;
            }
        }

        if (is_meet){
            while (head != slow)
            {
                head= head->next;
                slow = slow->next;
            }
            return slow;
        }
        return nullptr;
    }
};