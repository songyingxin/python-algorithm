#include <queue>

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void traversal(TreeNode *node){
    if(!node){
        return;
    }

    // 前序遍历
    traversal(node->left);
    // 中序遍历
    traversal(node->right);
    // 后序遍历
}

void Preorder(TreeNode * node){
    
}


void BFS(TreeNode * root){
    std::queue<TreeNode *> Q;
    Q.push(root);
    while(!Q.empty()){
        TreeNode *node = Q.front();
        Q.pop();
        // 打印  node 的值
        if (node->left){
            Q.push(node->left);
        }
        if(node->right){
            Q.push(node->right);
        }
    }
}