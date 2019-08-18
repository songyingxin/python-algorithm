## 1. 实现前缀树 -- 208
- 思路： 首先定义TrieNode ， child 表示该节点有多少种可能， path 表示有无字符串通过该节点， end 表示有无字符串以该节点为结尾
> - insert： 
> - search: 
> - startsWith: 

## 2. 添加与搜索单词 -- 211

- 思路：
> - add： 其与 Trie 树的实现差不多
> - search： 需要采用递归来做： search_trie(node, word)
> > - 当遍历len(word) == 0时，如果此时 node 的 end 属性 != 0 ， 则返回True， 否则，返回False
> > -  当word[0] 指向 '.'时：遍历node 的全部孩子， 如果孩子 != None， 则递归该word
> > - 当word[0] 在'a' - 'z'， 之间，则需要递归两个孩子： '.‘ 与 对应的字符