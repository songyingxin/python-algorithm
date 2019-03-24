
## 二分查找

假设表中元素按升序排列，将表中间位置关键字与查找关键字比较
> - 如果两者相等，则查找成功
> - 否则，利用中间位置将表分成前，后两个子表
>> - 如果中间位置的关键字大于查找关键字，则进一步查找前一字表
>> - 否则进一步查找后一子表


## 1. 插入位置

- 来源：[leetcode 35](https://leetcode-cn.com/problems/search-insert-position/)
- 问题： 给定一个排序数组nums（无重复元素）和一个目标值target，如果target在nums中出现，则返回target所在下标，如果target在nums里未出现，则返回target应该插入位置的数组下标，使得将target 插入数组nums后，数组仍有序。

### 思路1

采用二分查找，如果找到，则直接返回mid， 如果没找到，返回low

### 思路2

## 2. 区间查找 -- search_range

- 来源： **[leetcode 34](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)**
- 问题： 给定一个排序数组nums（nums中有重复元素）与目标值target， 如果target 在nums中出现， 则返回target所在区间的左右端点下标，[左端点，右端点], 如果target在nums里未出现，则返回[-1, 1]。
- 要求：算法时间复杂度为O(logn)

### 思考

1. 可否直接通过二分查找，很容易同时求出目标target所在区间的左右端点？
2. 若无法同时求出区间左右端点，则对目标target的二分查找增加怎样的限制条件，就可分别求出目标target所在区间的左端点，右端点？

### 思路

- 查找区间左端点时， 增加如下限制条件：当target == nums[mid]时，若此时**mid==0 或nums[mid-1] < target**， 则说明mid为区间左端点，返回；否则我们从 [:mid-1]进行二分

- 查找区间右端点时，增加如下限制条件：当 target == nums[mid]时， 若此时**mid == nums.size()-1  或 nums[mid+1] > target** ， 则说明mid 即为区间右端点， 否则从[mid+1:] 进行二分


## 3. 搜索旋转数组 -- search_rotate_array

- 来源：**[leetcode 33](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)**
- 问题:  给定一个排序数组nums（nums无重复元素），且nums可能以某个未知下标旋转，给定目标值target， 求target 是否在nums中出现，若出现返回所在下标，未出现返回-1.

- 要求： 时间复杂度为 O(logn)


**旋转数组性质： nums[begin ] > nums[end]**

### 分析

