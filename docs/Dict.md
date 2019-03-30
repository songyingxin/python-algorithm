## 定义

字典，又名符号表， 是一种存储键值对的数据结构，支持两种操作： 插入， 查找。

- 每个键值对应一个值
- 当表中存入的键值对与已有键值产生冲突， 新的值会替代旧的值
- 键值不能为空


## API 一览

API | 说明
--- | ---
ST() | 创建一张符号表
void put( Key key, Value value) | 将键值对存入表中
Value get(Key, key) | 获取键 key 对应的值
void delete(Key key) | 删除键Key
boolean contains(Key key) | 键 key 在表中是否右对应的值
boolean isEmapty() | 表是否为空
int size() | 表中键值对数量
Iterable<Key> keys() | 表中所有键的集合

