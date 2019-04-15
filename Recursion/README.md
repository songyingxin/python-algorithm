


---

**牛客**

## 汉诺塔问题
- 来源： https://www.nowcoder.com/questionTerminal/7d6cab7d435048c4b05251bf44e9f185

- 思路： 对于 from， mid， end 三个柱子， 
  > - 第一步：将 from中n-1 个元素移动到 mid中
  > - 第二步：将元素 n 从 from移到 mid中
  > - 第三步：最后将 n-1 个元素从 mid 移动到 to中