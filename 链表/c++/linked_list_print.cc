
/**
*  struct ListNode {
*        int val;
*        struct ListNode *next;
*        ListNode(int x) :
*              val(x), next(NULL) {
*        }
*  };
*/

class Solution
{
  public:
    vector<int> printListFromTailToHead(ListNode *head)
    {
        vector<int> result;
        stack<int> nodes;

        ListNode* pNode = head;
        while(pNode != nullptr)
        {
            nodes.push(pNode->val);
            pNode = pNode->next;
        }

        while(!nodes.empty())
        {
            result.push_back(nodes.top());
            nodes.pop();
        }

        return result;
    }
};

class Solution
{
  public:
    vector<int> result;
    vector<int> printListFromTailToHead(ListNode *head)
    {
        if(head != nullptr)
        {
            if(head->next != nullptr)
            {
                printListFromTailToHead(head->next);
            }
            result.push_back(head->val);
        }

        return result;
    }
};