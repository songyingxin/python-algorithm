# 第二章

### 1. 替换空格

- 来源： offer 5

- 思考： 一个空格字符在替换后变成'%', '2', '0' 三个字符，因此字符串会变长。

- 思路1： 空间复杂度 O(n)， 转化为列表，然后拼接列表， 用python 十分适合
- 思路2： 空间复杂度 O(1)， 首先计算出替换后的字符串长度。然后准备两个索引：index_origin, index_new； index_origin 指向原始字符串的末尾，index_new 指向替换之后的字符串的末尾。 从尾到头的用index_origin 遍历原始字符串，如果str[index_origin] != 空格， 则str[index_new] = str[index_origin]； 如果 str[index_origin] == 空格， 则分别复制 '0', '2', '%' 到str中, 直至 index_origin 遍历完毕。 适合 c++ 。

在合并两个数组或字符串时，如果从前往后复制每个数字或字符串需要重复移动多次，那么可以考虑从后往前复制，这样就能减少移动次数，从而提高效率。

- 扩展： 两个排序的数字 A1 与 A2， A1的末尾有足够多的空域空间容纳A2， 请将A2中所有数字插入到A1中，且所有的数字都是排序的。
- 思路： 从尾到头比较 A1 ， A2 的数字，将较大的数字复制到A1 中的合适位置

---

# 第三章

## 1. 正则表达式匹配 -- Re

- 来源：[offer 19](<https://www.nowcoder.com/practice/45327ae22b7b413ea21df13ee7d6429c?tpId=13&tqId=11205&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking>)

- 两种情况：第二个字符为 `*`， 第二个字符不为 `*`：
  - 第二个字符为 `*` ， 则当第一个字符匹配或第一个字符为`.` 时，有三种匹配方式： `s` 与 `pattern[2:]`， `s[1:]` 与 `pattern[2:]`， `s[1:]` 与 `pattern `
  - 第二个字符不为 `*`， 则当第一个字符是否匹配或为 `.` ， 此时有一种匹配方式：`s[1:]` 与 `pattern[1:]`

## 2. 表示数值的字符串 -- Re

- 来源： [offer 20](<https://www.nowcoder.com/practice/6f8c901d091949a5837e24bb82a731f2?tpId=13&tqId=11206&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路： 
  - e(E) 只能出现一次且不能再最后一个
  - 小数点不能重复出现或在 e(E) 之后出现
  - `+,-` 必须出现在开头或e的后一位

---

## 第四章

### 1. 字符串的排列 -- Re

- 来源： [offer 38](<https://www.nowcoder.com/practice/fe6b651b66ae47d7acce78ffdd9a96c7?tpId=13&tqId=11180&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路： DFS 的思路

---

## 第 五 章

### 1. 最长不含重复字符的子字符串 -- Re

- 来源： offer 48  leetcode 3
- 思路： 

### 2.  第一个只出现一次的字符

- 来源： [offer 50](<https://www.nowcoder.com/practice/1c82e8cf713b4bbeb2a5b31cf5b0417c?tpId=13&tqId=11187&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)

- 采用字典来做，{字符：次数}， 然后再遍历一次就可得到



---

## 第 六 章

### 1. 翻转单词顺序 

- 来源：  [offer 58 ](<https://www.nowcoder.com/practice/3194a4f4cf814f63919d0790578d51f3?tpId=13&tqId=11197&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)

- 思路1： 采用一个栈， 将每个翻转后的单词压入栈中，然后弹出形成字符串返回
- 思路2： 先翻转句子中所有字符； 再翻转每个单词中字符顺序

### 2. 左旋转字符串 

-  来源： [offer 58](<https://www.nowcoder.com/practice/12d959b108cb42b1ab72cef4d36af5ec?tpId=13&tqId=11196&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
-  思路1： 将前 [:num] 个字符与 [num+1:] 字符切分； 然后再[num+1:] + [num:] 连接
-  思路2： 先分别把[:num], [num+1:] 两部分翻转， 然后再将整个字符串翻转

---

## 第 七 章

### 1. 将字符串转化为整数

- [offer 67](<https://www.nowcoder.com/practice/1277c681251b4372bdef344468e4f26e?tpId=13&tqId=11202&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking>)  leetcode 8
- 思路： 此题主要考察边界问题

