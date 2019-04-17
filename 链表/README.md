
## 1. 反转链表

来源： leetcode 206

- **注意： 此处的head也存数据**

- 思路1：采用一个新的头结点new_head ， 依次访问原节点，将节点采用头插法插入到新节点中。
- 思路2： 采用一个新的头结点new_head ， 依次访问原节点，然后将节点逆序


## 2. 反转链表2

- 来源： **leetcode 92**

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

- 思路2： 快慢指针；如果快慢指针最终相遇则说明有环


## 5. 环形链表2 -- linked_list_cycle2

- 来源：[leetcode 142](https://leetcode-cn.com/problems/linked-list-cycle-ii/)
- 题目： 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

- 说明： 不允许修改给定的链表。

- 思路： 采用快指针step=2)，慢指针(step=1)， 如果慢指针与快指针相遇 ，则说明链表有环； 此时快指针回到初始节点处，step=1， 此时，快指针和慢指针会在初始结点处相遇， 此时我们就得到了初始结点。

![](http://ww1.sinaimg.cn/large/006gOeiSly1g0qpdd0o5lj30yo0lf7dj.jpg)


## 6. 链表划分 -- linked_list_partition

- 来源：[leetcode 86](https://leetcode-cn.com/problems/partition-list/)

- 题目：给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

- 要求：你应当保留两个分区中每个节点的初始相对位置。

- 思路：采用两个临时节点: less_head, more_head, 这两个节点不在链表中，这样分析会很简单。

## 7. 复制带随机指针的链表 -- linked_list_copy

**- 来源： [leetcode 138](https://leetcode-cn.com/problems/copy-list-with-random-pointer/)**

- 题目： 已知一个随机复杂链表，节点中有一个指向本链表任意某个节点的随机指针（可以为空），求这个链表的深度拷贝。

- 思路1：采用两个 map 来做， 其中map1 为{原节点地址:节点位置（第几个节点)}； map2 为 {节点位置：新链表节点}
- 思路2： 

## 8. 排序链表的合并 -- linked_list_merge

- 来源：[leeetcode 21](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

- 题目： 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

- 思路： 采用一个临时节点会很方便

## 9.  合并k个有序链表 -- k_linked_list_,merge

**- 来源：[leetcode 23](https://leetcode-cn.com/problems/merge-k-sorted-lists/)**
- 题目： 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

- 思路1： k个链表顺序合并k-1次(1,2合并，再与3合并)，此时的时间复杂度为 : 
$$
(n+n) + (2n+n) + ... + ((k-1)n + n) = (1+2+...+k-1)n + (k-1)n = (1+2+... + k)n - n = \frac{(k^2+k-1)}{2} * n = O(k^2*n)
$$

- 思路2： 将k*n个节点放到vector中，再将vector排序，然后将节点顺序相连。时间复杂度为：

$$
kN * logkN + kN = O(kN * logkN)
$$

- **思路3： 将k个链表进行分治，两两进行合并。 时间复杂度分析：**
  > - 第一轮，进行 k/2 次，每次处理 2n 个数字；
  > - 第二轮， 进行 k/4 次， 每次处理 4n 个数字
  > ...
  > - 最后一次， 进行 k/(2^logk) 次，每次处理 2^logk*N个值。
$$
2N * k / 2 + 4N * k/4 + ... + 2^logk * N *k /(2^logk) = Nk + ...+ Nk = O(kNlogk)
$$



## 参考

[1] 《 剑指offer》
[2]   牛客算法题
[3]   沐神课程