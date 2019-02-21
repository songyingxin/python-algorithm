## 什么是栈

栈实现的是一种后进先出， 先进后出(LIFO)的序列。栈中有两个操作：PUSH与POP。

## 栈的几种操作

操作 | 时间复杂度 | 说明
--- | --- | ---
push() |   | 添加一个元素
pop() |   | 从栈中删除最近添加的那个元素
is_empty() |   | 栈是否为空
size() |   | 栈的大小
top() |   | 查看栈顶元素

## 什么是队列？
队列实现的是一种先进先出(FIFO)的序列。队列中有两种操作： 入队与出队。

cpython 源码地址：https://github.com/python/cpython/blob/3.7/Lib/queue.py

## 基本操作

操作 | 时间复杂度 | 说明
--- | --- | ---
enqueue() |  |队列尾部添加一个元素
dequeue() |  |删除队列首部元素
is_empty() |  |判断队列是否为空
size() |   | 队列中元素数量
top() |   | 查看栈顶元素

--- 


## 练习题

### 1. 设计一个有getMin功能的栈： stack_min.py

#### 题目
> 实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作
#### 要求
> - pop， push， getMin 操作的时间都为O(1)
> - 设计的栈类型可以使用现成的栈结构

#### 解题思路
> 采用两个栈，一个用来保存当前栈中的元素，其功能与一个正常的栈没有区别，记为StackData；另一个栈用于保存每一步的最小值，这个栈记为 StackMin。

#### 实现方式 1

- 压入数据规则:

> 假设当前压入数据为new_num。则先将其压入StackData中，然后
> - 如果StackMin为空，则将new_num也压入到StackMin中
> - 如果不为空，则比较new_num 与 StackMin 栈顶元素，
>> - 如果 new_num > 栈顶元素，则StackMin不压入任何元素
>> - 如果 new_num <= 栈顶元素，则将new_num 压入到StackMin中

- 弹出数据规则

> - 弹出StackData中的栈顶元素，记为value，比较value 与StackMin的栈顶元素
>> - 若value == StackMin栈顶元素，StackMin弹出栈顶元素
>> - 若value > StackMin栈顶元素，stackMin不弹出栈顶元素，返回value

- 查询当前栈中最小值

返回StackMin的栈顶元素


#### 实现方式2：

- 压入数据规则：
> 假设当前压入数据为new_num。则先将其压入StackData中，然后
> - 如果StackMin为空，则将new_num也压入到StackMin中
> - 如果不为空，则比较new_num 与 StackMin 栈顶元素，
>> - 如果 new_num <= 栈顶元素，则将new_num 压入到StackMin中
>> - 如果 new_num > 栈顶元素，则把StackMin栈顶元素重复压入到StackMin，即在栈顶元素上再压如一个栈顶元素

- 弹出数据规则：

> 在stackData中弹出数据，记为value；弹出StackMiin的栈顶元素，返回value。

- 查询当前栈中的最小值操作

返回StackMin的栈顶元素

#### 方案1 与方案2 比较

- 相同点：
> 1. 都采用StackMin栈顶元素保存StackData每一步的最小值
> 2. 所有操作的时间复杂度都为O(1), 空间复杂度都为O(n)

- 不同点：
> - 方案1中StackMin压入时稍省空间，但是弹出操作稍费时间
> - 方案2中StackMin压入时稍省空间，但是弹出操作稍省时间