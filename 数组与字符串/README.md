## 1.   除自身以外数组的乘积

- 来源： leetcode 238
- 思路1： 先求乘积， 在整除。 需要注意 0 的情况
- 思路2： 先统计 nums[:i] 的乘积为 left [i]， 再统计 nums[i+1: ] 的乘积为 right[i]， 那么就有 output[i] = left[i] * right[i]


## 2. 寻找重复数

- 来源： leetcode 287
- 思路：快慢指针的思想
  > - 需要重看

## 3. 前 k 个高频元素

- 来源： leetcode 347

- 思路1：从左到右遍历，找到比当前数大的第一个数 -- 超时
- 思路2：用栈的思想

## 4. 盛最多水的容器

- 来源： leetcode 11
- 思路： 双指针

## 5. 合并区间

- 来源： leetcode 56
- 思路： 先排序

## 6. 连续的子数组和

https://blog.csdn.net/zxzxzx0119/article/details/81604489

- 来源： leetcode 523

### 思路1： DP

- sum[i][j]: 表示第i个元素到第j个元素的累加和
- sum[i][j]：sum[0][j]- sum[0][i] + nums[i]

### 思路2：哈希表




### 扩展1
- 题目：给定一个数组arr， **全是正数**； 求累加和等于 aim 的最长子数组，要求额外空间复杂度为 O(1), 时间复杂度为 O(N)

- 思路： 采用双指针， 因为有限定条件全是正数，因此可以采用双指针的思路，而上题就不可以。
> - left = 0, right = 0
> - 当 sum < target， 则
> - 当 sum > target,  则
> - 当 sum ==  target, 则 

### 扩展2 -- Hard

- 题目：给定一个数组 arr， 值可正，可负，可0； 求累加和小于等于target 的最长子数组，要求时间复杂度为 O(N)

- min_sum[i]: 以 nums[i]开始的的最小累加和
- min_sum_index[i]: 以 nums[i]开始的的最小累加和，此时它的右边界 index
- min_sum[i] = nums[i] if min_sum[i+1] > 0 else  nums[i] + min_sum[i+1]
- min_sum_index[i] = i if min_sum[i+1]>0 else min_sum_index[i+1]


## 7. 最长连续序列

- 来源： leetcode 128
- 思路：

## 8. 每日温度

- 来源： leetcode 739
- 思路： 单调栈： 
  - 入栈条件： 当前元素比栈顶元素小
  - 出栈条件： 遇到比自己大的温度


