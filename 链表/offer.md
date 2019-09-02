
## 第二章
### 1. 从头到尾打印链表

- 来源： [offer 6](https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?tpId=13&tqId=11156&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
- 题目：输入一个链表的头节点， 从尾到头反过来打印出每个节点的值。
- 思路1：空间复杂度O(n)， 采用一个列表保存链表所有节点，然后直接返回倒序数组。
- 思路2： 采用递归的思想来做。


## 第三章

### 1. 删除链表的节点

- offer 18   类似  leetcode 237
- 思路1：找到该节点的前一个节点，然后进行删除即可，时间复杂度O(n)
- 思路2：将该节点的下一个节点的值复制到该节点中，然后删除该节点的下一个节点。时间复杂度O(1). 
  如果输入节点为最后一个节点，则依旧需要找到该节点的前一个节点。
  如果链表中只有一个节点，则我们删除节点后还需要将链表头节点设置为nullptr

### 2. 删除链表中重复的节点 -- Re

- 来源：[offer 18](<https://www.nowcoder.com/practice/fc533c45b73a41b0b44ccba763f866ef?tpId=13&tqId=11209&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking>)
- 思路：维护两个指针： res 指向新链表的最后一个元素， tmp 用来遍历链表， 在遍历过程中，找到下一个不重复的节点，插入到 res 后面。 考虑到头节点也有可能被删除，因此建立一个新的头节点更容易处理。


### 3. 链表中的倒数第 k 个节点

- 来源： [offer 22](<https://www.nowcoder.com/practice/529d3ae5a407492994ad2a246518148a?tpId=13&tqId=11167&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking>)
- 思路： 设定一个指针，让该指针先走 k 步， 然后 两个指针一直走，直到第一个指针走到头。


### 4. 链表中环的入口节点

- 来源： [offer 23](<https://www.nowcoder.com/practice/253d2c59ec3e4bc68da16833f79a38e4?tpId=13&tqId=11208&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking>)
- 思路： 快慢指针。 快指针一次走两步，慢指针一次走一步，同时出发，在第一次相遇后，快指针回到起点，一次走一步，二者最终相遇的点就是环的入口节点。


### 5. 反转链表

- 来源： [offer 24](<https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=13&tqId=11168&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking>)
- 思路： 建立一个新的头结点，然后遍历链表，采用头插法将所有节点插入到新链表中

### 6. 合并两个排序的链表

- 来源： [offer 25](<https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?tpId=13&tqId=11169&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路：新建一个头节点，哪个小取哪个， 最后把非空的接在新链表后面

## 第四章

### 1. 复杂链表的复制 -- Re

- 来源： [offer 35](<https://www.nowcoder.com/practice/f836b2c43afc4b35ad6adc41ec941dba?tpId=13&tqId=11178&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>) 推荐看 [leetcode](<https://leetcode-cn.com/problems/copy-list-with-random-pointer/solution/fu-zhi-dai-sui-ji-zhi-zhen-de-lian-biao-by-leetcod/>)
- 思路：在创建复制节点的过程中，采用**字典**来映射旧节点与复制节点之间的联系

## 第五章

### 1. 两个链表的第一个公共节点

- 来源： [offer 52](<https://www.nowcoder.com/practice/6ab1d9a29e88450685099d45c9e31e46?tpId=13&tqId=11189&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路： 首先分别遍历两个链表，得到两个链表的长度 length1， length2， 然后让较长的链表先走 length - length2 步， 然后再一起走