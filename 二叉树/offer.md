
# 第二章
---

## 1. 重建二叉树 -- Re

- 来源： [offer 7](https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6?tpId=13&tqId=11157&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
- 思路： 与画树的思路一致，以 pre[0] 为头节点，根据 tin 划分左，右子树范围，分别递归简历
- 注意pre 与 vin的长度一致是一样的，重点就在于pre与vin的划分。

## 2. 二叉树的下一个结点 -- Re

- 来源： [offer 8](https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e?tpId=13&tqId=11210&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)

- 思路： 
  - 如果一个结点有**右子树**，则它的下一个结点就是**它的右子树中的最左子结点**； 
  - 如果**没有右子树**，且其为其父节点的**左子结点**， 则它的下一个结点就是它的父结点
  - 如果**没有右子树**， 且它为它父节点的**右子结点**， 则我们需要沿着指向父节点的指针一直向上遍历，直到找到一个它是该父节点的左子结点。此时，该父节点就是我们要找的下一个结点。


## 第三章

### 1. 树的子结构 -- Re

- 来源： [offer 26](<https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88?tpId=13&tqId=11170&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路：对于树 A 的每一个节点，判断节点值 与 B 的值是否相同
  - 如果相同， 则递归判断左子树，右子树是否分别相同

## 第四章

### 1. 二叉树的镜像

- 来源： [offer 27](<https://www.nowcoder.com/practice/564f4c26aa584921bc75623e48ca3011?tpId=13&tqId=11171&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路： 先交换当前节点的左右子节点， 然后递归交换左右子节点。

### 2. 对称的二叉树

- 来源：[offer 28](<https://www.nowcoder.com/practice/ff05d44dfdb04e1d83bdbdab320efbcb?tpId=13&tqId=11211&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking>)
- 思路： 判断左，右节点的值是否相等， 然后递归判断是否对称


## 第四章

### 1. 从上到下打印二叉树

#### 1. 不分行从上到下打印二叉树

- 来源： [offer 32](<https://www.nowcoder.com/practice/7fe2212963db4790b57431d9ed259701?tpId=13&tqId=11175&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路：本质上是层序遍历， 采用一个队列即可

### 2. 分行从上到下打印二叉树

- 来源： [offer 32](<https://www.nowcoder.com/practice/445c44d982d04483b04a54f298796288?tpId=13&tqId=11213&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路： 依旧是层序遍历 + 内循环

### 3. 之字形打印二叉树

- 来源： [offer 32](<https://www.nowcoder.com/practice/91b69814117f4e8097390d107d2efbe0?tpId=13&tqId=11212&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路： 层序遍历 + 内循环 + 设置一个 left_to_right 标志


### 4. 二叉树的后序遍历序列 -- Re

- 来源：[offer 33](<https://www.nowcoder.com/practice/a861533d45854474ac791d90e447bafd?tpId=13&tqId=11176&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路： 分析二叉搜索树的后序遍历的特性， 其**左子树 < 根 < 右子树**，且最后一个元素为根。 

### 5. 二叉树中和为某一值的路径 -- Re

- 来源： [offer 34](<https://www.nowcoder.com/practice/b736e784e3e34731af99065031301bca?tpId=13&tqId=11177&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路： DFS， 遍历每一条路径。


### 6. 二叉搜索树转化为双向链表 -- Re

- 来源：[offer 36](<https://www.nowcoder.com/practice/947f6eb80d944a84850b0538bf0ec3a5?tpId=13&tqId=11179&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 分析：搜索二叉树中，左子节点的总是小于父节点的值。右子节点的值总是大于父节点的值，因此，在二叉搜索树转化为排序双向链表时， 根节点的左指针指向左子树中的最右节点， 根节点的右指针指向右子树中的最左节点
- 思路： 先分别将左，右子树都转化为排序双向链表，然后再和根节点连接起来。

### 7. 序列化二叉树 -- Re

- 来源：[offer 37](<https://www.nowcoder.com/practice/cf7e25aa97c04cc1a68c8f040e71fb84?tpId=13&tqId=11214&tPage=4&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)

- 序列化： 按照前序(中序或后序)思路进行递归遍历
- 反序列化：

# 第六章
---

## 1. 二叉搜索树的第k大节点 -- 

- 来源： [offer 54](<https://www.nowcoder.com/practice/ef068f602dde4d28aab2b210e859150a?tpId=13&tqId=11215&tPage=4&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路 ： 一次中序遍历得到二叉搜索树的一个有序数组arr， 返回arr[k-1] 即可

## 2. 二叉树的深度

- 来源： [剑指offer 55](<https://www.nowcoder.com/practice/435fb86331474282a3499955f0a41e8b?tpId=13&tqId=11191&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking>)

- 思路： 树的深度 = max(左子树深度, 右子树深度) + 1
## 3. 平衡二叉树

- [offer 55](<https://www.nowcoder.com/practice/8b3b95850edb4115918ecebdf1b4d222?tpId=13&tqId=11192&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)

- 思路： 树为平衡二叉树 = 左子树为平衡二叉树 and 右子树为平衡二叉树 and abs(左子树深度 - 右子树深度) <= 1

# 第七章

---

## 1. 树中两个节点的最低公共祖先

- 来源：offer 68  leetcode 236
- 思路：

<https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/er-cha-shu-de-zui-jin-gong-gong-zu-xian-by-leetcod/>