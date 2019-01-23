
## 基础知识

- 随机访问, 可以在O(1) 时间内找到指定的元素
- 插入,删除操作需要移动大量元素


操作 | 最好时间复杂度 | 平均时间复杂度 | 最坏时间复杂度
--- | --- | --- | ---
插入 | O(1)  | $\sum_{i=1}^{n-1} p_i (n-i+1) = \frac{n}{2}$ | O(n) 
删除 | O(1) | $\sum_{i=1}^n p_i (n-i) = \frac{n-1}{2}$ | O(n)
按值查找 |  O(1) | $\sum_{i=1}^n p_i n = \frac{n+1}{2}$ | O(n)

## LeetCode

### 1. Move-zeros

- 网址： https://leetcode.com/problems/move-zeroes/
- 问题： 给定一个数组nums，写一个函数，将数组中的所有0移到数组的末尾，而维持其他非0元素的相对位置。如： [0,1,0,3,12] --> [1,3,12,0,0]
> - 要求1： You must do this in-place without making a copy of the array.
> - 要求2： Minimize the total number of operations.


- 思想： 将非0元素拿出来放到数组的前面，最后在数组的尾部补0。
> - simple： 非原地算法，采用另外一个数组保存非0元素，然后将该数组中的元素重写到源数组中，并将其余元素写为0
> - middle： 原地算法，设置一个 left 来表示来表示非0元素的个数，将[0...k]的元素都为非0元素，在最后将[k...] 的元素设为0
> - high： 原地算法，在遍历过程中，通过交换来一步到位， 且为了降低交互次数，只有在 i != left 时才交换。


### 2. Remove Element

- 网址： https://leetcode.com/problems/remove-element/
- 问题： 给定一个数组nums和一个数值val， 将数组中所有等于val的元素删除，并返回剩余元素个数， 如： nums=[3,2,2,3],val = 3 --> 返回2， 且nums中前两个元素为2
- 考虑问题：
> - 如何定义删除？ 从数组中去除？还是放在数组末尾？
> - 剩余元素的排列是否要保证原有的相对顺序 ？
> - 是否有空间复杂度的要求？

- 思路： 

### 3. Remove Duplicated from Sorted Array I

- 网址： https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- 问题： 给定一个有序数组，对数组中的元素去重，使得原数组的每个元素只有1个。返回去重后数组的长度值。 如： num = [1,1,2] --> 返回2，且nums的前2个元素为1和2


### 4. Remove Duplicated from Sorted Array II

- 网址：https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
- 问题： 给定一个有序数组，对数组中的元素去重，使得原数组的每隔元素最多保留2个。返回去重后数组的长度值。 如：nums=[1,1,1,2,2,3] --> 返回5， 且nums的前5个元素为1,1,2,2,3

---

### 5. sort colors

- 网址： https://leetcode.com/problems/sort-colors/
- 问题： 给定一个有n个元素的数组，数组中元素的取值只有0,1,2三种可能。为这个数组排序。如： [2,0,2,1,1,0] --> [0,0,1,1,2,2]
- 思路1： 计数排序，先分别统计0,1,2 的元素个数, 然后再在nums里写入。
- 思路2： 三路排序, 没有太搞明白


### 6. Merge Sorted Array  -- 88

- 网址： https://leetcode.com/problems/merge-sorted-array/
- 问题： 给定两个有序数组nums1， nums2， 将nums2的元素归并到nums1中
- 思路： 采用快排能够很快解决


### 7. Kth Largest Element in an Array -- 215

- 网址： https://leetcode.com/problems/kth-largest-element-in-an-array/
- 问题： 在一个整数序列中寻找第k大的元素， 如： [3,2,1,5,6,4],k=2 --> 结果为5

--- 

对撞指针

### 8. Two sum II - Input arrary is sorted  -- 167

- 网址：　https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
- 问题：　给定一个有序整型数组和一个整数target，　在其中寻找两个元素,使其和为target.返回这两个数的索引. 如: numbers=[2,7,11,15],target=9 --> 返回数字2,7的索引1,2(索引从1开始计算)
> - 如果没有解? 保证有解
> - 如果有多个解? 返回任意解

- 思路1: 暴力解法. 双层遍历, O(n), 不推荐
- 思路2: 二分查找思路,在内部循环中采用二分查找,时间复杂度为 O(nlogn)
- 思路3: 对撞指针思路, 利用有序的特性,多退少添

---
滑动窗口

### 9. Minimum Size Subarray -- 209

- 网址: https://leetcode.com/problems/minimum-size-subarray-sum/
- 问题: 给定一个整型数组和一个数字s,找到数组中最短的一个连续子数组,使得连续子数组的数字和sum >= s, 返回这个最短连续子数组的长度, 如果没有找到,则返回0. 如: s=7, nums = [2,3,1,2,4,3] --> 最短子数组 [4,3], 返回值为2

> - 什么叫子数组
> - 如果没有解怎么办? 返回0
> - 如果有多个解怎么办?

- 思路1: 暴力解法: 遍历所有的连续子数组[i..j], 计算和sum,验证sum >= s, 时间复杂度为 $O(n^3)$
- 思路2: 不定长窗口滑动. 时间复杂度为O(n), 空间复杂度为O(1)


### 10. Longest Substring Without Repeating Characters

- 网址: https://leetcode.com/problems/longest-substring-without-repeating-characters/
- 问题: 


## 牛客算法

### 1. classify_array

- 题目： 给定一个数组arr和一个数num， 请把小于等于num的数放在数组的左边，大于num的数放在数组的右边。
- 要求： 空间复杂度为O(1)， 时间复杂度为O(N)
- 思路： 设定一个left=-1 表示起始时，小于num的左指针位置， 从头到尾遍历数组，如果arr[i] < num，则arr[left+1], arr[i] = arr[i], arr[left+1], 否则，跳过。


### 2. 荷兰国旗问题

- 问题： 给定一个数组arr 和一个数num， 请把小于num的数放在数组的左边， 等于num的数放在数组的中间，大于num的数放在数组的右边
- 要求： 空间复杂度为O(1)， 时间复杂度为O(N)
- 思路： 设定一个left = -1, right = len(arr), 从头到尾遍历数组，如果arr[i] < num， 则 arr[left+1], arr[i] = arr[i], arr[left+1]; 如果 arr[i] == num， 跳过; 如果 arr[i] > num， 则 arr[right-1] arr[i] = arr[i], arr[right-1], 此时i 不变, 接着重复判断 arr[i] 。 

### 3. 最大差值

- 问题： 给定一个无序数组，求如果排序之后，相邻两数的最大差值，要求时间复杂度O(N), 且要求不能用非基于比较的排序

- 思路： 
> - 划分桶： 桶数为N+1（N为数组长度）, 先遍历一遍数组，找到最大值max，最小值min， 按照最大值，最小值划分为N个桶
> - 装桶： 遍历数组，将元素放入对应的桶中， 桶中只保存是否为空， 最小值，最大值，其余数扔掉
> - 找桶： 最大差值一定不来自一个桶内部，且不一定来自空桶两侧的桶

## 剑指offer

### 1. 

- 题目：给定给定一个有序数组arr,和一个整数aim,请返回哪两个位置的数可以加出aim来（唯一）。
- 举例：arr = {2,7,11,15}, target = 9, 那么返回 [0,1]， 因为arr[0] + arr[1] = 9
- 思路1 -- 穷举法：
