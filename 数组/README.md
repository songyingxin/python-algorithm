## 1.   除自身以外数组的乘积

- 来源： leetcode 238
- 思路1： 先求乘积， 在整除。 需要注意 0 的情况
- 思路2： 先统计 nums[:i] 的乘积为 left [i]， 再统计 nums[i+1: ] 的乘积为 right[i]， 那么就有 output[i] = left[i] * right[i]


