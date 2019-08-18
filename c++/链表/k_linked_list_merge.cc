#include <vector>

#include "linked_list.h"

bool cmp(const ListNode *a, const ListNode *b)
{
    return a->val < b->val;
}

class Solution
{
  public:
    ListNode *mergeKLists(std::vector<ListNode *> &lists)
    {
        std::vector<ListNode *> node_vec;
        for (int i = 0; i < lists.size(); i++)
        {
            ListNode *head = lists[i];
            while (head)
            {
                node_vec.push_back(head);
                head = head->next;
            }
        }
        if (node_vec.size() == 0)
        {
            return NULL;
        }
        std::sort(node_vec.begin(), node_vec.end(), cmp);
        for (int i = 1; i < node_vec.size(); i++)
        {
            node_vec[i - 1]->next = node_vec[i];
        }
        node_vec[node_vec.size() - 1]->next = NULL;
        return node_vec[0];
    }
};

ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
{
    ListNode new_head(0);
    ListNode *ptr = &new_head;

    while (l1 && l2)
    {
        if (l1->val < l2->val)
        {
            ptr->next = l1;
            l1 = l1->next;
        }
        else
        {
            ptr->next = l2;
            l2 = l2->next;
        }
        ptr = ptr->next;
    }

    while (l1)
    {
        ptr->next = l1;
        l1 = l1->next;
        ptr = ptr->next;
    }

    while (l2)
    {
        ptr->next = l2;
        l2 = l2->next;
        ptr = ptr->next;
    }
    ptr->next = nullptr;

    return new_head.next;
}

class Solution
{
  public:
    ListNode *mergeKLists(std::vector<ListNode *> &lists)
    {
        if (lists.empty()){
            return nullptr;
        }

        if (lists.size() == 1){
            return lists[0];
        }

        if(lists.size() == 2){
            return mergeTwoLists(lists[0], lists[1]);
        }

        std::vector<ListNode *> vec1;
        std::vector<ListNode *> vec2;

        mid = lists.size()/2;

        for (int i=0; i < mid; i++){
            vec1.push_back(lists[i]);
        }

        for (int i = mid; i < lists.size(); i++){
            vec2.push_back(lists[i]);
        }

        ListNode *l1 = mergeKLists(vec1);
        ListNode *l2 = mergeKLists(vec2);

        return mergeTwoLists(l1, l2); 
    }
};