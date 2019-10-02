
# 第三章
---
## 1. 数值的整数次方

- 来源： [offer 16](<https://www.nowcoder.com/practice/1a834e5e3e1a4b7ba251417554e07c00?tpId=13&tqId=11165&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)

### 思路1：

主要考察边界条件：
> - base = 0 exponent < 0时， 报错
> - exponent > 0, exponent < 0, exponent = 0 时 


## 2. 打印从1到最大的n位数

- 来源： [offer 17]()
- 陷阱： n很大时的溢出问题， n <= 0 时的错误输入问题

### 思路1：
为了避免溢出问题，需要通过字符串来进行操作，在字符串上模拟数字的加法。

- 首先定义一个长度为 n+1 的字符串，并将每一个数字都初始化为 '0'
- 在字符串表达的数字上模拟加法
- 把字符串表达的数字打印出来

### 思路2： 

采用数字排列的方法：


## 10. 不使用新变量，交换两个变量的值

- 基于加减法

  ```
  a = a + b
  b = a - b
  a = a - b
  ```

- 基于异或运算

  ```
  a = a ^ b
  b = a ^ b
  a = a ^ b
  ```