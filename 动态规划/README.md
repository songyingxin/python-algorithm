## 动态规划问题套路

第一步： 确定dp[i] 或 dp[i][j] 代表什么意思？
第二步： 探索边界值，从边界值中寻找规律
第三步： 确定状态转移方程
第四步： 验证状态转移方程的有效性

---
Easy 级别


## 1. 除数博弈
- 来源： leetcode 1025

### 分析
- dp[i]:  黑板上数字为 i 的情况下， Alice 的输赢情况， 赢：True， 输： False
- dp[0] = False, dp[1] = False, dp[2] = True
- dp[i] = True 当 j =  1, ... i-1 中有一个满足 i % j == 0 and dp[i-j]==False时； 其余情况均为 False


## 2. 爬楼梯

- 来源： leetcode 70
- 思路： 
  - dp[i]：爬到第i个台阶有多少种方法
  - dp[1] = 1, dp[2] = 2
  - dp[i] = dp[i-1] + dp[i-2]

## 3. 打家劫舍

- 来源： leetcode 198
- 思路：
  - dp[i]: 前 i 个房屋所能获取的最多财宝数
  - dp[i] = max(dp[i-1], dp[i-2] + nums[i])


## 4. 最大子段和

- 来源： leetcode 53
- 思路：
  - dp[i]: 以 nums[i] 为结尾的最大子段和
  - dp[i] = max(dp[i-1] + nums[i], nums[i])



---
Medium

## 1. 找零钱

- 来源： leetcode 322
- 思路：
   - dp[i]：面值为 i 的钞票所需要的最少钞票数量
   - dp[i] = min(dp[i-j] for j in nums) + 1
   - 注意： 边界条件的处理

## 2. 三角形最小路径和

- 来源： leetcode 120
- 思路：自底向上
  - dp[i][j]: 到 第 i行 第 j 列所需的最小路径和
  - dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
  - 返回 dp[0][0]

## 3. 最长上升子序列

- 来源： leetcode 300
- 思路：
  - dp[i] : 以 nums[i] 为结尾的最长上升子序列
  - dp[i] = max(dp[i], dp[j] + 1 ) for j in 0..i-1 if nums[i] > nums[j]

## 4. 最小路径和

- 来源： leetcode 64
- 思路：
  - dp[i][j]: 达到 nums[i][j] 时的最少路径
  - dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + nums[i][j] 


---
Hard

## 1. 地下城游戏

- 来源： leetcode 174
- 思路：由底向上
  - dp[i][j]: 到达 i,j 位置需要最少的血量
  - dp[i][j] = max(1, dp[i+1][j], dp[i][j+1]) - dungeon[i][j]

















---
Medium 级别






## 1. 最小路径和

- 来源： leetcode 64

- 思路：
  > - dp[i][j]：代表到第i行第j列时的最小路径和
  > - dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + nums[i][j]

## 2. 打家劫舍2

- 来源： leetcode 337
- 思路1：dfs 问题 -- 会超时
- 思路2： 动态规划, 树型dp

## 3. 完全平方数

- 来源： leetcode 279
- 思路1： 动态规划 -- 超时，真奇怪
  > - dp[i]: 表示组成 i 的完全平方数最少的个数
  > - dp[i] =  min(dp[i], dp[i-j*j] + 1)

- 思路2： 四平方定理: 任何一个正整数都可以表示成不超过四个整数的平方之和。那么对于正整数 n， 必定满足 n = 4 ^a(8b + 7)


## 4. 最佳买卖股票时机含冷冻期 -- 难

- 来源： leetcode 309

- 思路： 动态规划
  > - sell[i]: 到第 i 天为止最后一个操作是卖出所对应的最大利润
  > - buy[i]:到第 i 天为止最后一个操作是买入所对应的最大利润
  > - cooldown[i]: 到第 i 天为止最后一个操作是冷冻所对应的最大利润
  > - sell[i] = max(sell[i-1], buy[i-1] + prices[i])
  > - buy[i] = max(buy[i-1], cooldown[i-1] - prices[i])
  > - cooldown[i]=max(cooldown[i-1],max(sell[i-1],buy[i-1])).

## 5. 分割等和子集 -- 比较难

- 来源： leetcode 416
- 思路： 动态规划
  > - dp[i][j] : 从数组 [0,j] 子区间挑选一些正整数，使得这些数的和能否等于 j
  > - dp[i][j] = dp[i-1][j]  or (nums[i] <= j and dp[i-1][j-nums[i]] )

## 6. 最长上升子序列

- 来源： leetcode 300
- 思路：动态规划
  > - dp[i]: [0,i] 这个区间内必须包含 nums[i] 时的最长上升子序列的长度
  > - dp[i] = max(dp[i], dp[j] + 1):  向前遍历找出比 i 元素小的元素 j


## 7. 单词拆分

- 来源： leetcode 139
- 思路： 动态规划
    > - dp[i]:  s[0:i] 是否可以由 wordDict 组成
    > - dp[i] = dp[i-j] and s[j:i] in word_dict,  j in 0,,i-1

## 8. 目标和 -- 很难

- 来源： leetcode 494
- 思路1： DFS

## 9. 和为 k 的子数组

- 来源： leetcode 560
- 思路： dp 为字典
  > - dp[(i, sum) ]: 以 nums[i] 结尾的，和为sum的连续子数组个数
  > - dp[(i, sum)] = dp[(i-1, sum-nums[i])] or 0


## 10. 编辑距离

- 来源： leetcode 72
- 思路：
  > - dp[i][j] ： word1的前 i 个字母和 word2的前 j 个字母之间的编辑距离
  > - if word1[i] == word2[j], dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] - 1)
  > - if word1[i] != word2[j], dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
