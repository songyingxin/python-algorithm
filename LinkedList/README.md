
## 面试题6： 逆序打印链表 [1] -- linked_list_print

- 题目： 输入一个链表的头结点，从尾到头的顺序返回一个数组。

### 思路1： 

- 思想： 从头到尾依次遍历链表，将每个节点的值放到一个栈中。 遍历结束后，再从栈顶逐个输出节点的值。

- 时间复杂度 O(n), 空间复杂度O(n)

### 思路2：

- 思想： 采用递归的方法。 我们没访问到一个节点时， 先递归输出其后面的节点，再输出该节点自身。

- 问题： 如果链表非常长，会导致函数调用的层级很深，从而可能导致栈溢出。

### 单元测试

- 链表有多个节点
- 链表只有一个节点
- 特殊输入测试： head = nullptr


## 面试题18： 删除链表的节点 -- 



---


## 1. 链表逆序 -  linked_list_reverse

来源： [leetcode 206](https://leetcode-cn.com/problems/reverse-linked-list/)

- 题目： 反转一个单链表

### 思路：

采用一个新的头结点new_head ， 依次访问原节点，将节点采用头插法插入到新节点中。
**注意： 此处的head也存数据**

## 2. 链表逆序 - linked_list_part_reverse

- 来源： [leetcode 92](https://leetcode-cn.com/problems/reverse-linked-list-ii/)

-  题目： 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

- 举例：输入 1-2-3-4-5-NULL, m=2,n=4； 输出：1-4-3-2-5-NULL

- 思路：
  > - 查找关键节点： 1. 逆置段头结点前驱 ； 2. 逆置段逆置后尾节点； 3. 逆置段逆置后头节点； 4. 逆置段尾节点的后继

- 具体过程：
  > 1.  将head向前移动m-1个位置，head指向开始逆置的节点，记录该节点的前驱 - pre_head以及该节点 - modify_list_tail
  > 2.  从 head 开始，逆置 change_len = n-m+1 个节点， 最终head指向逆置段尾节点的后继， new_head 指向逆置区的最后一个节点即逆置后的头节点
  > 3. 将pre_head 与 new_head 连接， modify_list_tail 与head 连接

**注意当m==1时的特殊情况**

## 3. 链表相交 -- intersection_of_linked_list

- 来源： [leetcode 160](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)
- 题目： 一只链表A的头结点指针headA， 链表B的头结点指针headB， 两链表相交，求两连败交点对应的节点

- 要求：
  > - 如果俩链表没有交点，则返回nullptr
  > - 在求交点过程中，不可以破坏链表的结构或修改链表的数据域
  > - 可以确保传入的链表A和链表B没有任何破坏
  > - 实现算法尽可能时间复杂度 O(n), 空间复杂度O(1)

- 思路1： 采用集合，将A链表中节点对应的指针插入set，然后看看B链表中有没有一样的指针
- 思路2： 先计算两个链表的长度，然后较长链表先移动 len_a - len_b 个位置，然后俩链表一起移动

## 4. 环形链表 -- linked_list_cycle

- 来源 : [leetcode 141](https://leetcode-cn.com/problems/linked-list-cycle/)

- 题目：给定一个链表，判断链表是否有环

- 思路1：采用set， 不断遍历链表， 如果当前元素在集合中出现过，说明，链表中有环。


## 参考

[1] 《 剑指offer》
[2]   牛客算法题
[3]   沐神课程