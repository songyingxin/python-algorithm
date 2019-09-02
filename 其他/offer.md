## 1. 求 1+2+...+n

- 来源： offer 64
- 题目： **求1+2+...+n。 要求不能使用乘除法， for， while， if， else， switch， case 等关键字及条件判断语句。**
- 思路1： 采用构造函数

## 2. 不用加减乘除做加法

- 来源：offer 65
- 题目： 写一个函数，求两个整数之和，要求在函数体内不得使用 "+", '-', '*', "/"， 四则运算符号。
- 二进制思想：采用异或的思想。


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
