



## 第五章
---

## 1. 数组中出现次数超过一半的数字

- 来源： [offer 39](<https://www.nowcoder.com/practice/e8a1b01a2df14cb2b228b30ee6a92163?tpId=13&tqId=11181&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)

### Partition 思路

- 分析： 当对数组排序后，位于数组中间的数字一定就是那个出现次数超过数组长度一半的数字。 那么问题就可以转化为找到数组中任意第 k 大的数字， 我们可以采用快排中的 Partition 思路。

### 数组特点思路

- 分析： 
- 思路：从头到尾遍历数组，**保存两个值**：数组中的一个数字， 次数。 当我们遍历到下一个数字时：
  - 如果下一个数字和我们之前保存的数字相同， 则次数+1
  - 如果下一个数字和我们之前保存的数字不同， 则次数-1
  - 若次数为0， 则我们保存下一个数字，并把次数设为1

  最后还需要检测 res 最终出现的次数是否大于一半

## 2. 最小k个数 -- Re

- 来源： [offer 40](<https://www.nowcoder.com/practice/6a296eb82cf844ca8539b57c23e6e9bf?tpId=13&tqId=11182&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)

### 思路1：Partition 

随机快排的思想， 找到划分点index， 
> - 如果 index == k-1, 则， 返回[:index]； 
> - 如果 index > k-1， 则在[:index-1]处在进行partition； 
> - 如果 index < k-1， 则在[index+1:] 进行partition。

### 思路2：大根堆思想

**采用一个大小为k的大根堆来存储最小的k个数字。**

从头到尾遍历数组，如果元素比堆顶大，则弹出堆顶，并将该元素塞入。

## 3. 数据流中的中位数 -- Re

- 来源： [offer 41](<https://www.nowcoder.com/practice/9be0172896bd43948f8a32fb954e1be1?tpId=13&tqId=11216&tPage=4&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)

- 思路：大根堆与小根堆思想。 大根堆中所有数据都要小于小根堆的数据。

  > -  如果大根堆，小根堆长度相等，则把数据与大根堆堆顶比较

## 5. 1-n 整数中1 出现的次数

- 来源： offer 43  leetcode 233
- 思路：


## 6.  数字序列中某一位数字
- 来源： offer 44  [leetcode 400](<https://leetcode-cn.com/problems/nth-digit/>)
- 分析： 
  - 1-9 有 9 个数， 10-99 有 20 * 9 个数， 100-999 有 300 * 9 个数， 因此可以得出所在位数规律： $9 * 10 ^{i-1} * i$

- 思路：
  - 先计算 nth 需要多少位数字
  - 找到具体的数字，接着找出数字中的某个值

## 7. 把数组排成最小的数

- 来源： [offer 45](<https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993?tpId=13&tqId=11185&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路： 对于两个数 n，m 如果nm < mn， 则将n放在m前面.

## 8. 把数字翻译成字符串

- 来源： offer 46 leetcode 91
- 思路： 
  - dp[i]： str[0...i] 的编码方法总数
  - 分情况讨论：
    - s[i] == '0'，  if str[i-1] == '1' or '2'， dp[i] = dp[i-2]， 否则返回 0
    - s[i-1] == '1'， dp[i] = dp[i-1] + dp[i-2]
    - s[i-1] == '2' and '1' <= s[i] <= '6', dp[i] = dp[i-1] + dp[i-2]

## 9. 数组中的逆序对

- 来源： [offer 51](<https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5?tpId=13&tqId=11188&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)  

- 思路： 归并排序的时候，合并时统计逆序对


# 第六章
---
## 1. 在排序数组中查找数字

- 来源： [offer 53](<https://www.nowcoder.com/practice/70610bf967994b22bb1c26f9ae901fa2?tpId=13&tqId=11190&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)

**数字在排序数组中出现的次数**

- 思路： 目的是找到该数字第一次出现的位置和最后一次出现的位置，这部分可以采用二分查找法

**0-n-1 中缺失的数字**

- 思路1： 求和， $s1 = \frac{n(n-1)}{2}$  , s2 = sum(nums)， 返回 s1 - s2
- 思路2： 目的是找到第一个 index != nums[index] 的数字， 通过二分查找来找到该数字

**数组中数值和下标相等的元素**

- 思路： 二分查找

## 2. 数组中只出现一次的两个数字

- 来源： [offer 56](<https://www.nowcoder.com/practice/e02fdb54d7524710a7d664d082bb7811?tpId=13&tqId=11193&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)  leetcode 540

- 分析： 异或运算的性质： 任何一个数字异或它自己都等于0

- 思路： 从头到尾依次异或数组中的每个数字，那么最终得到的结果就是两个只出现一次的数字的异或记过，而这个结果的二进制表示中至少有一位为1。 

  我们找到第一个为1的位的位置，记为第 n 位。 我们现在以第n位是不是1为标准将原数组中的数字分为两个子数组，那么此时出现了两次的数字肯定被分配到同一子数组。 然后我们依次异或每个子数组，找出子数组中只出现一次的数字。 最后，返回这两个数字。

## 3. 数组中唯一只出现一次的数字  -- 未找到 oj

- 题目： 在一个数组中除一个数字只出现一次外，其余数字都出现了三次，请找出那个只出现一次的数字。

- 思路： 如果一个数字出现了三次， 则它的二进制上的每一位都出现了三次，我们将所有数字的二进制表示的每一位都加起来； 如果某一位能被3整除，只出现一次的数字该位为0， 否则为1

## 4. 和为s的数字

- 来源： offer 57

### 1. 和为s的两个数字

- 来源： [offer 57](<https://www.nowcoder.com/practice/390da4f7a00f44bea7c2f3d19491311b?tpId=13&tqId=11195&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)

- 思路： 采用left， right 指针分别指向最左端，最右端。
  - 如果arr[left] + arr[right] > target, right--
  -  如果 arr[left] + arr[right] < target, left++
  -  如果 arr[left] + arr[right] == target, 返回 left, right。

### 2. 和为s的连续正数序列

- 来源： [offer 57](<https://www.nowcoder.com/practice/c451a3fd84b64cb19485dad758a55ebe?tpId=13&tqId=11194&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路：采用small， big 分别表示序列的最小值与最大值。 初始 `small=1, big=2`：
    - 如果从small...big的序列和 > s， 则small++
    - 如果small到big的序列和 < s ，则big++
    - 若等于则打印。 直至增大到small == (1+s)/2 为止

## 5. n 个骰子的点数

- 来源： offer 60 无 oj

- 思路： 动态规划

  - `dp[n][s]`： n 个骰子点数和为 s 的排列情况总数

  - 状态转移方程：
    $$
    dp[n][s] = dp[n-1][s-1] + dp[n-1][s-2] + ... + dp[n-1][s-6]
    $$


## 5. 扑克牌的顺子

- 来源： [offer 61](<https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4?tpId=13&tqId=11198&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路：
  - 首先将数组排序；然后统计数组中0的个数； 
  - 最后统计排序后的数组中相邻数字之间的空缺总数。
  - 如果空缺的总数小于或等于0的个数，则这个数组就是连续的，反之，不连续。 如果排序后有相邻元素相等， 则不连续。
## 6. 圆圈中最后剩下的数字 -- Hard

**约瑟夫问题**

- 来源： offer 62


- 思路：

```
f(n,m) = 0, if n == 1
f(n,m) = (f(n-1,m) + m) % n, if n > 1
```

```
第一个被删除的数字为 k = (m-1) % n
删除前x与删除后的数字映射为： p(x) = (x-k-1) % n   p(x) 的逆映射 = (x + k + 1) % n
那么有 f(n,m) = f(n-1, m) = p逆[f(n-1,m)] = [f(n-1,m) + k + 1] % n = [f(n-1,m) + m] % n
```

## 7. 股票的最大利润 

- 来源： offer 63  leetcode 121



- 思路：从头到尾遍历数组， 在扫描到第i个数字时， 记住之前 i-1 个数字中的最小值，然后计算最大利润即可


## 6. 构建乘积数组

- 来源： [offer 66](<https://www.nowcoder.com/practice/94a4d381a68b47b7a8bed86f2975db46?tpId=13&tqId=11204&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking>)


- 思路： 
