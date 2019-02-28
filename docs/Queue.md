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