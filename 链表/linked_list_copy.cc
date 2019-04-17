#include "linked_list.h"

class Solution
{
  public:
    RandomListNode *copyRandomList(RandomListNode *head)
    {
        std::map<RandomListNode *, int> node_map;
        std::vector<RandomListNode *> node_vec;
        RandomListNode *ptr = head;
        int i = 0;
        while (ptr)
        {
            node_vec.push_back(new RandomListNode(ptr->label));
            node_map[ptr] = i;
            ptr = ptr->next;
            i++;
        }
        node_vec.push_back(0);
        ptr = head;
        i = 0;
        while (ptr)
        {
            node_vec[i]->next = node_vec[i + 1];
            if (ptr->random)
            {
                int id = node_map[ptr->random];
                node_vec[i]->random = node_vec[id];
            }
            ptr = ptr->next;
            i++;
        }
        return node_vec[0];
    }
};