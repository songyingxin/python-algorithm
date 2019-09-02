
## 知识点

把一个整数减去1之后再和原来的整数做位与运算，得到的结果相当于将整数二进制表示中最右边的 1 变成 0. 

# 第二章
---

## 1. 二进制中 1 的个数

- 来源： [offer 15](<https://www.nowcoder.com/practice/8ee967e43c2c4ec193b040ea7fbb10b8?tpId=13&tqId=11164&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking>)

### 思路1：

不右移n， 而是首先用 n 与1 做位运算， 判断n的最低位是不是1， 接着把1左移一位得到2， 再与n做位运算， 以此类推。

### 思路2：???

**将一个整数减去1， 再和原整数做与运算，会将该整数最右边的1变成0， 该整数二进制有多少个1， 就可以进行多少次这样的操作**

扩展很有意思，需要再看