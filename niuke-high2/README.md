
**第一章**

## 1. KMP算法




## 2. Manacher 算法



## 3. BFPRT 算法
最大k个数， 最小k个数


---

**第二章**

## 1. 滑动窗口最大值

- 来源： leetcode 239

- 思路： 采用**双端队列结构**， 双端队列元素存放是从大到小的， 双端队列中存储 index。 
  > - 当right 指针向右移动时， arr[right] 与 双端队列中小的位置依次比较，如果 arr[right]>= ？， 则弹出双端队列中小元素， 再将 right, arr[right]插入双端队列中
 > - 当 left 指针向左移动时， 查看双端队列大的一端中元素的index是否过期， 如果过期（left > index)，则弹出该元素.

## 3. 

- 题目： 给定数组arr， 整数num， 返回共有多少个子数组满足以下情况：
  > - max(arr[i...j]) - min(arr[i...j]) <= num

- 要求： 时间复杂度O(N)

- 思路： 采用两个双端队列， 一个保存移动窗口的最大元素， 一个保存移动窗口的最小元素。分别以0，1, ..., n-1 为起点，进行移动窗口，直到窗口无法移动（再移动就无法保证<=num)， 那么以 i 为起点的满足子数组有 right - i + 1 个

## 4. 单调栈结构

**解决一个数组中每个元素， 左边离他最近的比它大的， 右边最近的离它大的数， 时间复杂度O(N)**

- 思路： 一个栈， 保持其从底到顶是从大到小的顺序


## 5. 构造maxtree

 定义二叉树的节点为：

```
public class Node{
    public int value;
    public Node left;
    public Node right;

    public Node(int data){
        this.value = data;
    }
}
```
一个数组的maxTree 定义如下：
- 数组必须没有重复元素
- maxTree是一棵二叉树，数组的每个值对应一个二叉树节点
- 包括maxTree树在内且在其中的每一棵子树上，值最大的节点都是树的头

无重复元素的数组arr， 写出生成这个数组的maxTree 的函数，要求如果数组长度为N， 则时间复杂度为O(N)，空间复杂度为O(N)


## 6. 最大子矩阵的大小

- leetcode 85


---

**第三章**

## 1. 二叉树Morris遍历

- 介绍一种时间复杂度为O(N)， 空间复杂度为O(1)的二叉树遍历方式，N为二叉树节点个数。

思路：
- 来到的当前节点，记为cur， 如果cur无左孩子， 则cur = cur.right
- 如果cur有左孩子， 找到cur左子树上最右的节点，记为mostright：
  > - 如果mostright的right指针指向空，则让其指向cur， cur = cur.left
  > - 如果mostright 的right指针指向cur， 让其指回空， cur = cur.right

## 3. 搜索二叉树

