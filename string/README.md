
## 1. 无重复字符的最长子串

- 来源：[leetcode 3](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

- 问题： 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

### 思路1 

从头到尾遍历字符串，当进入一个新字符的时候， 我们获得包含该新字符的最长子串，然后将该子串与之前的子串比较，返回较长的子串。

## 思路2

采用双指针的思想， 利用一个哈希表来记录字符是否出现， 用word来记录当前最长子串。 
从头到尾遍历字符串， 
> - 如果字符没有出现过， 则直接 word += s[i]
> - 如果字符之前出现过，则begin指针要向后移动，直到该字符的出现次数为1。

## 2. 重复的DNA序列

- 来源：[leetcode 187](https://leetcode-cn.com/problems/repeated-dna-sequences/)
- 问题： 将DNA序列看做只包含 ['A', 'C', 'G', 'T'] 四个字符的字符串，给一个DNA字符串，找到所有长度为10的且出现超过一次的子串。


### 思路1

枚举DNA字符串中所有长度为10的子串，将其插入到哈希map中， 并记录子串数量； 遍历哈希map， 将所有出现超过一次的子串存储到结果中。算法复杂度O(n)。

### 思路2

我们分别采用[0,1,2,3](二进制形式) 来表示 ['A', 'C', 'G', 'T'] 四个字符， 故长度为10 的DNA序列可以用20个bit的整数表示。

1. 设置全局整数哈希 int g_hash_map[1048576]; 1048576 = 2^20， 表示所有长度为10的DNA序列
2. 将DNA字符串的前10个字符使用左移位运算转换为整数key,g_hash_map[key]++.
3. 


## 3. 最小窗口子串

- 来源：[leetcode 76](https://leetcode-cn.com/problems/minimum-window-substring/)
- 题目： 给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。
- 举例： 输入：S = "ADOBECODEBANC", T = "ABC"； 输出："BANC"

