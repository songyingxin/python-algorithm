#include <vector>

using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution
{
  public:
    TreeNode *reConstructBinaryTree(vector<int> pre, vector<int> vin)
    {
        int pre_len = pre.size();
        if (pre_len == 0)
        {
            return NULL;
        }

        vector<int> left_pre, right_pre, left_in, right_in;
        TreeNode* head = new TreeNode(pre[0]);

        int index = 0;  // 中序遍历中根节点的位置
        for (int i=0; i< pre_len; i++)
        {
            if (vin[i] == pre[0])
            {
                index = i;
                break;
            }
        }

        // 划分pre， vin为左子树与右子树
        for(int i=0; i < index; i++)
        {
            left_in.push_back(vin[i]);
            left_pre.push_back(pre[i+1]);
        }

        for(int i=index+1; i<pre_len; i++)
        {
            right_in.push_back(vin[i]);
            right_pre.push_back(pre[i]);
        }

        head->left = reConstructBinaryTree(left_pre, left_in);
        head->right = reConstructBinaryTree(right_pre, right_in);

        return head;
    }
};