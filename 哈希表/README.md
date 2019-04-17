## 1. 最长回文串

- 来源： [leetcode 409](https://leetcode-cn.com/problems/longest-palindrome/)
- 问题：给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
- 要求： 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

### 思路

- 采用一个哈希表来统计字符串中所有的字符数量
- 最长回文偶数字符长度 max_length = 0
- 是否有中心的 flag = 0
- 遍历哈希表，如果字符数为偶数，max_length += cout ; 若为奇数， max_lenght += cout-1, flag = 1
- 最终返回 max_length + flag

## 2. 单词模式

- 来源： [leetcode 290](https://leetcode-cn.com/problems/word-pattern/)

- 问题： 已知字符串pattern 与字符串 str， 确认str是否与pattern匹配。 匹配代表字符串str中的单词与pattern中的字符一一对应。
- 举例： pattern = "abba", str = "dog cat cat dog" ， 二者匹配

### 思路

1. 当pattern中的字符数与str中的单词数不一致时，返回False
2. 从头到尾遍历str中的单词：
   > - 如果单词不曾在 哈希表 help 的 keys()中出现过， 则需要判断 此时 pattern[i]是否 已经用过。 如果没有用过，则 help[word] = pattern[i]； 如果已经用过，则返回False
   > - 如果单词在哈希表help中出现过，则判断此时 help[word] == patternp[i]。 如果不相等，返回False



## 3.  字母异位词分组

- 来源：[leetcode 49](https://leetcode-cn.com/problems/group-anagrams/)
- 问题： 已知一组字符串，将所有字母异位词组合在一起。 字母异位词指的是字母相同，但排列不同的字符串。
- 举例： ["eat", "tea", "tan", "ate", "nat", "bat"], 其输出是：[["ate","eat","tea"], ["nat","tan"],["bat"]]

### 思路1

采用一个vector存储每个字符串排序后的结果，然后采用一个hashtable来做映射， key为排序后的字符串， value为排序后是key的原字符串。

### 思路2

哈希表以26个字符数量(一个长度为26的vector， 统计单词中各个字符的数量) 为key， 以字符串向量(vector<string>)为value， 存储各个字符数量相同的字符串。

- 对于每一个字符串strs[i]， 统计其中的各个字符的数量，存储至vec
- 若vec未出现在anagram中，设置vec到一个空字符串向量的映射
- 将strs[i] 添加至字符串向量 anagram[vec] 中

