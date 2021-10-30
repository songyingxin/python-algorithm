



### 1. 复杂链表的复制 -- Re

- 来源： [offer 35](<https://www.nowcoder.com/practice/f836b2c43afc4b35ad6adc41ec941dba?tpId=13&tqId=11178&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>) 推荐看 [leetcode](<https://leetcode-cn.com/problems/copy-list-with-random-pointer/solution/fu-zhi-dai-sui-ji-zhi-zhen-de-lian-biao-by-leetcod/>)
- 思路：在创建复制节点的过程中，采用**字典**来映射旧节点与复制节点之间的联系

## 第五章

### 1. 两个链表的第一个公共节点

- 来源： [offer 52](<https://www.nowcoder.com/practice/6ab1d9a29e88450685099d45c9e31e46?tpId=13&tqId=11189&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路： 首先分别遍历两个链表，得到两个链表的长度 length1， length2， 然后让较长的链表先走 length - length2 步， 然后再一起走