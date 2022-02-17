


## 4.  二叉查找树的编码和解码

- 来源：[leetcode 449](https://leetcode-cn.com/problems/serialize-and-deserialize-bst/)
- 题目：给定一个二叉查找树，实现对该二叉查找树编码，解码功能。 编码是将该二叉查找树转为字符串， 解码是将字符串转为二叉查找树。
  
### 思路

- 二叉查找树编码为字符串
  将二叉查找树前序遍历， 遍历时将整型的数据转化为字符串， 并将这些字符串数据采用特殊字符进行连接。

- 将字符串解码为二叉查找树
  将字符串按照分隔符拆分， 将第一个数字构建为二叉查找树的根节点， 后面各个数字构建二叉查找树时的操作依次插入，最后返回根节点即可。


## 5. 逆序数

- 来源：**[leetcode 315](https://github.com/selfteaching/the-craft-of-selfteaching/tree/master/markdown)**
- 题目： 已知数组nums， 求新数组count， count[i] 代表在nums[i] 右侧且比 nums[i] 小的元素个数

### 思考分析

将元素按照原数组逆置后的顺序插入到二叉排序树中， 如何在元素插入时，计算已有多少个元素比当前插入元素小。


### 思路

按照原数组逆置构建二叉查找树， 并记录每个节点中左子树的个数，然后将所有左子树的个数相加即可。



## 1. 计算右侧小于当前元素的个数 -- right_small

- **来源：[leetcode 315](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/)**