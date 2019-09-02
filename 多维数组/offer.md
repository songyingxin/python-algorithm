## 第三章

### 1. 顺时针打印矩阵

- 来源： [offer 29](<https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a?tpId=13&tqId=11172&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking>)
- 思路：依次打印外圈数字，
  - 第一步：从左到右打印一行
  - 第二步：从上到下打印一列
  - 第三步： 从右到左打印一行
  - 第四步： 从下到上打印一列

- 坑： 需要注意排除一行一列的情况

---

## 第五章

### 1. 礼物的最大价值

- 来源： offer 47 leetcode 64

- 思路： 动态规划：
  - `dp[i][j]`: 到达 `nums[i][j] ` 的最小路径
  - `dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + nums[i][j]`

