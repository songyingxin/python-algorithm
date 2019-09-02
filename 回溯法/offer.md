## 第二章
---

## 1. 矩阵中的路径 -- Re

- 来源： [offer 12](<https://www.nowcoder.com/practice/c61c6999eecb4b8f88a98f66b273a3cc?tpId=13&tqId=11218&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking>)
- 思路：对每一个点进行回溯，考虑到访问过的元素不能再次访问，因此需要维护一个 flag 矩阵来表示是否访问过。

## 2. 机器人的运动范围 -- Re

- 来源：[offer  13](<https://www.nowcoder.com/practice/6e5207314b5241fb83f2329e89fdecc8?tpId=13&tqId=11219&tPage=4&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
 - 思路： 采用回溯法， 如果机器人能够进入坐标(i, j)的格子， 再判断它能否进入4个相邻的格子 (i, j-1), (i-1, j), (i, j+1), (i+1, j)






**回溯法依旧不熟**