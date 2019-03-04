
## 1. 利用队列实现栈 -- queue_to_stack

- 来源：[leetcode  225](https://leetcode-cn.com/problems/implement-stack-using-queues/)
- 问题： 使用队列实现栈的下列操作： push(x), pop(), top(), empty()
- 思路:： 用两个队列实现栈， data 用于入元素， help 用于帮助返回元素：
  > - push: 将元素存入data中
  > - pop: 
    >> - 如果data非空, 将 data中元素入队列到 help中(除最后一个元素)，输出最后一个元素; data 与 help 交换
    >> - 如果data为空，则抛出异常

- 思路2：同样采用两个队列， data 用于入元素， help 用于帮助返回元素。 不过，此时复杂操作在push端：
   > - pop: 直接将data中的第一个元素 pop
   > - push: 先将元素放入help中， 然后将data中的元素依次放入help中， 交换 data， help