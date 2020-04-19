# 学习笔记
## 知识点总结
#### 第3课 数组、链表、跳表
1. Array 数组：
   1. 内存管理器分配连续的内存空间，随机访问时间复杂度: O(1)
   2. Array Insert 操作：找到指定位置，将指定位置之后的元素往后移动，然后将目标元素插入指定位置。时间复杂度: O(n)
   3. Array Delete 操作：找到指定位置并移除元素，将指定位置之后的元素往前移动。时间复杂度为: O(n)
2. Linked List 链表：
   1. 可以弥补数组的缺陷（频繁增删的场景下，数组的效率并不高）
   2. 单链表增删节点：只需移动节点的Next指针，时间复杂度为：O(1)。***此处疑问：要找到要新增节点的位置或要删除的节点，还是需要遍历的，这个时候，时间复杂度应该是O(n)的吧？***
   3. 随机访问（查询）：需要遍历到指定节点，时间复杂度为：O(n)
   4. Java中的链表实现：为双向链表结构
3. Skip List 跳表：
   1. **只能用于表中元素是有序的情况**
   2. 对标平衡二叉树和二分查找
   3. 因为要维度新增的索引，删除及新增操作都要调整所有的索引，所以时间复杂度为：O(logn)，空间复杂度为：O(n)
   4. 一维数据结构查找加速思考方向：升维思想，空间换时间
4. 工程应用：
   1. LRU Cache（最近最少使用）缓存机制：基于Linked List实现
   2. Redis：Skip List

### 第4课 栈、队列、双端队列、优先队列
1. Stack & Queue 栈与队列：
   1. Stack：Last in-First out(LIFO，先进后出)
   2. Queue：First in-First out(FIFO，先进先出)
   3. 插入、删除元素时间复杂度：O(1)
   4. Stack & Queue 均不支持随机访问，查找元素的时间复杂度均为：O(n)
   5. **如果一件事具有最近相关性，则可以考虑用Stack解决**
   ```python
   # 栈的实现
   class Stack(object):
      def __init__(self):
         self.__list = []

      def push(self, item):
      """添加元素到栈顶"""
         self.__list.append(item)

      def pop(self):
         return self.__list.pop()

      def peek(self):
         if self.__list:
            return self.__list[-1]
         else:
            return None

      def is_empty(self):
         return self.__list == []

      def size(self):
         return len(self.__list)

   # 队列的实现
   class Queue(object):
      def __init__(self):
         self.__list = []

      def enqueue(self, item):
         self.__list.append(item)

      def dequeue(self):
         return self.__list.pop(0)

      def is_empty(self):
         return self.__list == []

      def size(self):
         return len(self.__list)
   ```
2. Deque（Double End-Queue） 双端队列：
   1. 栈与队列的结合体，首尾均可进行添加与删除
   2. 插入与删除时间复杂度：O(1)
   3. 查询时间复杂度：O(n)
   ```python
   # 双端队列的实现
   class Deque(object):
      def __init__(self):
         self.__list = []

      def add_front(self, item):
         self.__list.insert(0, item)

      def add_rear(self, item):
         return self.__list.append(item)

      def pop_front(self):
         return self.__list.pop(0)

      def pop_rear(self):
         return self.__list.pop()

      def is_empty(self):
         return self.__list == []

      def size(self):
         return len(self.__list)
   ```
3. Priority Queue 优先队列：
   1. 插入操作：O(1)
   2. 取出操作：O(logN)-按照元素的优先级取出
   3. 底层具体实现的数据结构较为多样和复杂：heap、bst、treap


## 作业
1. 用新的API改写Deque的代码
   
   ```java
   // 旧接口的实现
   Deque<String> deque = new LinkedList<String>();
   deque.push("a");
   deque.push("b");
   deque.push("c");
   System.out.println(deque);

   String str = deque.peek();
   System.out.println(str);
   System.out.println(deque);

   while(deque.size()>0){
       System.out.println(deque.pop());
   }
   System.out.println(deque);

   // 新接口的实现
   Deque<String> deque = new LinkedList<String>();
   deque.addLast("a");
   deque.addLast("b");
   deque.addLast("c");
   System.out.println(deque);

   String str = deque.peek();
   System.out.println(str);
   System.out.println(deque);

   while(deque.size()>0){
       System.out.println(deque.pop());
   }
   System.out.println(deque);
   ```
2. Java中的Queue与Priority Queue的源码分析
   1. Java中的Queue为一个接口，定义了三组接口：`add & offer,remove & poll,element & peek` 
   2. 前者可能会抛异常，而对应情况下后者只会返回特殊值以表示操作失败
   3. Priority Queue的实现

## 一些参考链接
1. Java 的 [Priority Queue 源码](http://fuseyism.com/classpath/doc/java/util/PriorityQueue-source.html)
2. Java 的 [Queue 源码](http://fuseyism.com/classpath/doc/java/util/Queue-source.html)
3. [为啥 redis 使用跳表(skiplist)而不是使用 red-black？](https://www.zhihu.com/question/20202931)
4. [LRU缓存算法](https://www.jianshu.com/p/b1ab4a170c3c)
5. [Redis 设计与实现（第一版）](https://redisbook.readthedocs.io/en/latest/index.html)

