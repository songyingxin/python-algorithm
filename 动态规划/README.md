## 1. 最小路径和

- 来源： leetcode 64

- 思路：
  > - dp[i][j]：代表到第i行第j列时的最小路径和
  > - dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + nums[i][j]