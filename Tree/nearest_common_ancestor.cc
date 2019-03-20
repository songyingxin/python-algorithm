#include <vector>
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution
{
  public:
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q)
    {
        std::vector<TreeNode *> path_p;
        std::vector<TreeNode *> result_p;
        int finish_p = 0;

        std::vector<TreeNode *> path_q;
        std::vector<TreeNode *> result_q;
        int finish_q = 0;
        preorder(root, p, path_p, result_p, finish_p);
        preorder(root, q, path_q, result_q, finish_q);

        int path_len = 0;
        if (result_p.size()  < result_q.size()){
            path_len = result_p.size();
        }
        else{
            path_len = result_q.size();
        }

        TreeNode *result = 0;
        for(int i = 0; i < path_len; i++){
            if (result_p[i] == result_q[i]){
                result = result_p[i];
            }
        }
        return result;
    }

  private:
    void preorder(TreeNode *node, TreeNode *search, std::vector<TreeNode *> &path, std::vector<TreeNode *> &result, int &finish)
    {
        if (!node || finish)
        {
            return;
        }

        path.push_back(node);
        if (node == search)
        {
            finish = 1;
            result = path;
        }

        preorder(node->left, search, path, result, finish);
        preorder(node->right, search, path, result, finish);

        path.pop_back();
    }
};