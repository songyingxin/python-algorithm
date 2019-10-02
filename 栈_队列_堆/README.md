

---

Easy

## 1. 利用队列实现栈 

- 来源： **leetcode 225**

- 思路:： 用两个队列实现栈， data 用于入元素， help 用于帮助返回元素：
  > - push: 将元素存入data中
  > - pop: 
  > >- 如果data非空, 将 data中元素入队列到 help中(除最后一个元素)，输出最后一个元素; data 与 help 交换
  > >- 如果data为空，则抛出异常

- 思路2：同样采用两个队列， data 用于入元素， help 用于帮助返回元素。 不过，此时复杂操作在push端：
   > - pop: 直接将data中的第一个元素 pop
   > - push: 先将元素放入help中， 然后将data中的元素依次放入help中， 交换 data， help

## 2. 利用栈实现队列

- 来源： leetcode 232

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

## 3. 最小栈 

- 来源： **leetcode 155**

- 思路：采用两个栈：data存储元素， help存储栈最小元素
  > - push: data直接push进元素， help push当前最小元素
  > - pop: data pop栈顶， help pop 栈顶
  > - top: 返回 data栈顶
  > - min: 返回help栈顶

## 4. 有效的括号

- 来源： **leetcode 20**
- 思路： 

---

Medium

## 1. 验证栈序列

- 来源： **leetcode 946**

## 2. 返回数组中第k大的数

- 来源： **leetcode 215**

- 思路：采用大小为k的最小堆，堆中最终保存k个最大的元素，此时堆顶元素就是第k个最大的元素

  > - 当堆中元素个数小于k时，新元素直接进堆，
  > - 否则，比较堆顶元素，如果堆顶元素较小，则弹出堆顶，将新元素加入堆中


---

Hard

## 1.   基本计算器

- 来源： **leetcode 224**

- 思路： 采用两个栈： 数字栈，操作符栈，分析两种情况：**有括号与无括号的情况**

## 2.  数据流的中位数 

- 来源： **leetcode 295**

采用一个大根堆max_heap和一个小根堆min_heap，核心思想是小根堆中的元素要大于大根堆中的元素。
 - addNum: 
  > - 如果 max_heap 为空，则将num插入到max_heap 中
  > - 如果 max_heap 非空，若 max_heap.size() == min_heap.size() ， 则比较num与max_heap 的堆顶，如果 num > max_heap.top()，则将num push到max_heap 中，否则push到min_heap 中
  > - 如果 max_heap 非空，若 max_heap.size() > min_heap.size()，则比较num与max_heap.top()， 若num>max_heap.top()， 则将num push到小根堆中； 否则，将min_heap中的堆顶push到max_heap 中
  > - 如果 max_heap 非空，若 max_heap.size() < min_heap.size()， 则比较num 与min_heap.top()， 若 num < min_heap.top()， 则将mum push到大根堆中；否则，将max_heap堆顶push到min_heap 中

- findMeidan:
  > - 如果max_heap.size() == min_heap.size(), 则返回俩堆堆顶的平均值
  > - 否则，哪个堆大，返回哪个堆的堆顶
