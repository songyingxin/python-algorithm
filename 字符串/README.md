
Easy

## 1. 单词规律

- 来源：leetcode 290
- 思路： 采用哈希表+集合来做



---
Medium

## 1. 同字符词语分组

- 来源： leetcode 49
- 思路1：
  - 先对每个字符串内部排序，那么字母相同的字符串已经完全一样了
  - 然后采用哈希表进行遍历

- 思路2：以26个字母的字符数量为 key， 以字符串为val， 存储各个字符数量相同的字符串


## 2. 无重复字符的最长子串

- 来源： leetcode 3
- 思路： 

https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/






## 1. 移掉 k 位数字
- 来源：leetcode 402


## 2. 字符串解码

- 来源： leetcode 394

- 思路： 采用栈来做



---
Hard
## 1. 基本计算器

- 来源： leetcode 224
- 思路：栈 + 贪心算法， 将字符串中的数字依次入栈，若当前字符大于栈顶数字，弹出栈顶并更新 k 值直至 k 为0。 若循环结束 k 还不为 0， 则去掉栈顶剩余的 k 个元素