## 1. 转圈打印矩阵

- 来源： https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a?tpId=13&tqId=11172&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking  - 剑指offer 原题

- 要求： 额外空间复杂度 O(1)
- 思路： 采用左上角(start_row,start_col)，右下角(end_row, end_col)。 先打印外圈的边界，然后采用递归的思想，递归的打印内圈的边界。

## 2. 旋转图像

- 来源：leetcode 48

- 思路： 采用左上角(start_row,start_col)，右下角(end_row, end_col)，先将外圈的数据交换，然后递归的进行内圈的交换。这需要观察数据得出交换的规律。
  四个点分别为： `arr[start_row][start_col+i]， arr[start_row+i][end_col], arr[end_row][end_col-i], arr[end_row-i][start_row]`

## 3. “之”字形打印矩阵

- 来源： 
- 题目： **给定一个矩阵matrix,按照“之”字形的方式打印这个矩阵**
- 举例: 
  ```
  1     2   3   4 
  5     6   7   8 
  9     10  11  12
  ```
  “之”字形打印的结果为:
  ```
  1     2   5   9
  6     3   4   7
  10    11  8   12
  ```

- 思路： 采用两个指针a， b， 起始 a=b=0， a往右走， 走不动了向下走， b往下走， 走不动了向右走。 a， b 同时走动。


## 4. 在行，列都排好序的矩阵中找数

- 来源： leetcode 74， leetcode 240

- 思路： 从右上角开始遍历
  > - if arr[i][j] > val , j--
  > - if arr[i][j] < val , i++

## 5. 不同路径

- 来源： leetcode 62
- 思路：二维动态规划


## 6. 岛屿数量

- 来源： leetcode 200
- 思路： dfs, bfs
  
## 7. 搜索二维矩阵2

- 来源：leetcode 240
- 思路： 