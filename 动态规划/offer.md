
# 第二章
---
## 1. 斐波那契数列

- 来源： [offer 10](<https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking>)， 此题本质上是动态规划的简化， 已经给出了状态转移方程，主要是看如何省略 dp 数组，仅维护两个变量来维持整个动态方程
- 输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）

$$
f(n)= \begin{cases} 0 \qquad n=0 \\ 1  \qquad n=1 \\ f(n-1) + f(n-2) \qquad n>1 \end{cases}
$$

## 2. 青蛙跳台阶问题

- 来源： [offer 10](<https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=13&tqId=11161&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)， 本题考的是你有没有能力将问题转化为动态规划问题，并写出状态转移方程。
- n=1 时， 1种跳法, 即 f(1) = 1
- n=2 时， 2种跳法, 即 f(2) = 2
- n>2 时， 第一次跳的时候有两种选择：
> - 第一次只跳1级，则此时跳法数目 = 后面剩下n-1级的跳法数目 f(n-1)
> - 第一次只跳2级，则此时跳法数目 = 后面剩下的 n-2 级台阶的跳法数目 f(n-2)
> 因此有 f(n) = f(n-1) + f(n-2)

### 3. 变态跳台阶

- 来源： [offer 10](<https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387?tpId=13&tqId=11162&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路： 我们可以用归纳法推出： $f(n) = f(1) + ... + f(n-1) + 1 =  2^{n-1}$， 如果可能，推一遍更好。

### 4. 矩形覆盖

- 来源： [offer 10](<https://www.nowcoder.com/practice/72a5a919508a4251859fb2cfb987a0e6?tpId=13&tqId=11163&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 动态规划，状态转移方程：
> - n =1: f(n) = 1
> - n =2: f(n) = 2
> - n > 2: f(n) = f(n-1) + f(n-2)


## 5. 剪绳子

- 来源： [offer 14](<https://leetcode-cn.com/problems/integer-break/>) 类似 leetcode 343
- 题目： **给你一根长度为n的绳子，请把绳子剪成m段(m,n 都是整数， n>1, m>1)， 每段绳子的长度记为 k[0], k[1]，...，k[m]。 请问k[0] * ... *k [m] 可能的最大乘积是多少？**

### 思路1：动态规划

- dp[i]： 长度为 i 的绳子剪成若干段各段长度乘积的最大值

```
dp[i] = max(dp[1] * dp[i-1], ..., dp[i-1]*dp[1])
```

### 思路2： 贪婪算法

如果按照如下策略剪绳子， 则得到的各个绳子的长度乘积最大：
- n>=5时， 尽可能多剪长度为3的绳子
- n = 4 时， 将绳子剪成长度为2的两段

---

## 第五章

### 1. 丑数

- 来源： [offer 49](<https://www.nowcoder.com/practice/6aa9e04fc3794f68acf8778237ba065b?tpId=13&tqId=11186&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路：动态规划


# 第六章
---

## 1. n个骰子的点数 -- 未找到oj

- 来源： offer 60
- 题目： **把n个骰子仍在地上， 所有骰子朝上一面的点数之和为s。 输入n， 打印所有s的所有可能的值出现的概率。**

- 分析： 骰子和最小为n， 最大为6n， 所有排列数有$6^n$。 我们要求出每个点数和出现的概率，然后除以$6^n$ 即可。

### 思路1：递归

将骰子分为两堆，第一堆只有1个（1-6中的任意一个数），另一堆有 n-1 个。 我们需要计算1-6的每一种点数和剩下n-1个筛子来计算点数和。 以此递归， 直至剩下一个骰子。

我们采用一个长度为6n-n+1 的数组将和为s的点数出现的次数保存到数组的第 s-n个元素里

### 思路2： 基于循环

采用两个数组来存储骰子点数的每个和出现的次数。 

在第一轮循环种， 第一个数组中的第n个数字表示筛子和为n出现的次数； 下一轮循环中， 加上一个 新的筛子， 则此时和为n的骰子出现的次数 = 上一轮循环中骰子点数和为 n-1, n-2, n-3, n-4, n-5, n-6 的次数的总和

- 测试用例：
  > - 功能测试： 1， 2， 3， 4， 个筛子的各个点数的概率
  > - 特殊输入测试： 0
  > - 性能测试： 11


## 2. 把数字翻译成字符串 -- 未找到oj
- 来源： offer 46
- 题目： 给定一个数字，我们按照如下规则把它翻译成字符串： 0 翻译成“a”， “1” 翻译成 “b”， ..., 25 翻译成“z“。 一个数字可能有多少种翻译。
- 举例： 12258有5种翻译： "bccfi", "bwfi", "bczi", "mcfi", "mzi"


## 3. 礼物的最大价值 -- 未找到oj

- 来源： offer 47
- 题目： 在一个 m * n 的棋盘的每一格斗放有一个礼物，每个礼物都有一定的价值（大于0）。 你可以从棋盘左上角开始拿格子里的礼物，并每次向左或向下移动一格， 直到到达棋盘的右下角。 给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物。
- 思路： 动态规划

## 4. 最长不含重复字符的子字符串

- 来源： offer 48
- 题目： 请从字符串中找出一个最长的不包括重复字符的子字符串，计算该最长子字符串的长度。假设字符串中只包含 'a'-'z'的字符。 
- 举例： 字符串 'arabcacfr'， 最长的不含重复字符的子字符串为 'acfr'， 长度为4

## 5. 丑数
- 来源： offer 49
- 题目：只包含因子 2， 3， 5 的数称为丑数。 求从小到大的顺序的第1500个丑数。
