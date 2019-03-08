
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


## 2. 利用栈实现队列 -- stack_to_queue

- 来源：[leetcode 232](https://leetcode-cn.com/problems/implement-queue-using-stacks/)
- 题目： 使用栈实现队列的以下操作：push(), pop(), peek(), empty()

- 思路1： 采用两个栈来实现队列: data, help
  > - push: 直接将数据push到data中
  > - pop: 如果help非空，则help pop一个元素； 如果help为空， 则先将data中元素push到help中，help再pop元素
  > - top： help非空，则返回help栈顶元素； help为空，将data中元素push到help中再返回help栈顶元素
  > - empty： 如果help，data都为空，则返回 true

- 思路2： 同样采用两个栈来实现队列： data， help
    > - push: 先将data中元素push到help中， 然后将xpush到help， 最后再将help中的元素push到data中
    > - pop: 直接 data.pop()
    > - peek(): 返回data.top()
    > - empty(): 返回data.empty()


## 3. 最小栈 -- min_stack

- 来源： [最小栈](https://leetcode-cn.com/problems/min-stack/)

- 题目： 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈： push, pop, top, getMin

- 思路1：采用两个栈：data存储元素， help存储栈最小元素
  > - push: data直接push进元素， help push当前最小元素
  > - pop: data pop栈顶， help pop 栈顶
  > - top: 返回 data栈顶
  > - min: 返回help栈顶

## 4. 合法的出栈序列 -- check_stack

- **来源：[poj 1363](http://poj.org/problem?id=1363)**
- 题目：已知从1-n的数字序列，按顺序入栈，每个数字入栈后即可出栈，也可在栈中停留，等待后面的数字入栈出栈后，该数字再出栈，求该数字序列的出栈序列是否合法？

- 思路1： 采用一个额外的栈S来模拟序列order中的出栈入栈情况
   > 按元素1-n顺序，将元素push到栈中， 每push一个元素，检查是否与 order首元素相同，若相同，则弹出队列首元素，弹出S的栈顶元素，直至俩元素不同结束。 若最终栈为空，则说明序列合法，否则不合法

## 5.   基本计算器 -- calculator

- **来源： [leetcode 224](https://leetcode-cn.com/problems/basic-calculator/)**

- 题目：实现一个基本的计算器来计算一个简单的字符串表达式的值。字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

- 要求： 假设所有表达式都有效； 不要使用库函数 eval

- 思路： 采用两个栈： 数字栈，操作符栈，分析两种情况：**有括号与无括号的情况**

## 6. 返回数组中第k大的数 -- kth_max_element

- 来源：[leetcode 215](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)

- 题目：在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

- 思路：采 用大小为k的最小堆，堆中最终保存k个最大的元素，此时堆顶元素就是第k个最大的元素
  > - 当堆中元素个数小于k时，新元素直接进堆，
  > - 否则，比较堆顶元素，如果堆顶元素较小，则弹出堆顶，将新元素加入堆中


## 7.  数据流的中位数 -- find_median

-  **来源：[leetcode 295](https://leetcode-cn.com/problems/find-median-from-data-stream/) **
-  题目： 设计一个数据结构，该数据结构动态的维护一组数据，且支持如下操作：
   > - void addNum(int num):  从数据流中添加一个整数到数据结构中。
   > - double findMedian() : 返回目前所有元素的中位数。

- 思路1： 采用数组，每次添加元素或寻找中位数时对数组排序，再计算结果
  > - 在添加元素时排序，addNum 复杂度是O(n), findMedian 复杂度为O(1)
  > - 在查询中位数时排序，addNum 复杂度 O(1), findMedian 复杂度O(nlogn)
  若添加元素或查询中位数是随机操作，共n词操作，则整体的时间复杂度最佳为 $O(n^2)$

### 思路2： 

采用一个大根堆max_heap和一个小根堆min_heap，核心思想是小根堆中的元素要大于大根堆中的元素。
 - addNum: 
  > - 如果 max_heap 为空，则将num插入到max_heap 中
  > - 如果 max_heap 非空，若 max_heap.size() == min_heap.size() ， 则比较num与max_heap 的堆顶，如果 num > max_heap.top()，则将num push到max_heap 中，否则push到min_heap 中
  > - 如果 max_heap 非空，若 max_heap.size() > min_heap.size()，则比较num与max_heap.top()， 若num>max_heap.top()， 则将num push到小根堆中； 否则，将min_heap中的堆顶push到max_heap 中
  > - 如果 max_heap 非空，若 max_heap.size() < min_heap.size()， 则比较num 与min_heap.top()， 若 num < min_heap.top()， 则将mum push到大根堆中；否则，将max_heap堆顶push到min_heap 中

- findMeidan:
  > - 如果max_heap.size() == min_heap.size(), 则返回俩堆堆顶的平均值
  > - 否则，哪个堆大，返回哪个堆的堆顶

  