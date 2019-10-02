

# 第二章
---

## 1. 两个栈实现队列

- 来源： [offer 9](<https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?tpId=13&tqId=11158&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
  - push： 直接将元素直接存入 stack1 中
  - pop: 如果stack2为空，则将stack1 中元素压入到stack2中，再pop； 如果非空，则直接pop。
## 2. 用两个队列实现一个栈
- [offer 9](<https://leetcode-cn.com/problems/implement-stack-using-queues/>)
- 两个队列：data， help
> - push： 直接将元素存入data中
> - pop： 将data 中的元素依次 pop到help中，直至data中只剩下一个元素， 然后弹出该元素， data， help互换


## 第三章

### 1.  包含 min 函数的栈

- 来源： [offer 30](<https://www.nowcoder.com/practice/4c776177d2c04c2494f2555c9fcc1e49?tpId=13&tqId=11173&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路： 维护两个栈： min_stack, core_stack ，min_stack 维护最小元素

### 2. 栈的压入，弹出序列

- 来源： [offer 31](<https://www.nowcoder.com/practice/d77d11405cc7470d82554cb392585106?tpId=13&tqId=11174&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking>)
- 思路：用一个栈来模拟这个过程


