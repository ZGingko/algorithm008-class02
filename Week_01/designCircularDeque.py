class MyCircularDeque(object):
    """
    641. 设计循环双端队列
        你的实现需要支持以下操作：

        MyCircularDeque(k)：构造函数,双端队列的大小为k。
        insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
        insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
        deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
        deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
        getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
        getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
        isEmpty()：检查双端队列是否为空。
        isFull()：检查双端队列是否满了。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/design-circular-deque
    """

    def __init__(self, size: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.length=0
        self.size=size
        self.data=[-1]*size
        self.front = 0
        self.rear = 0
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.length == self.size:
            return False   
        if self.isEmpty():
            self.data[self.front] = value
        else:
            self.front = (self.front -1) % self.size
            self.data[self.front] = value        
        self.length += 1  
        return True

        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.length == self.size:
            return False
        if self.isEmpty():
            self.data[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.data[self.rear] = value        
        self.length+=1
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.data[self.front] = -1
        self.front = (self.front + 1) % self.size                
        self.length -= 1
        if self.isEmpty():
            self.rear = self.front
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.data[self.rear] = -1
        self.rear = (self.rear - 1) % self.size
        self.length -= 1
        if self.isEmpty():
            self.front = self.rear
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.data[self.front]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.data[self.rear]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.length==0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.length == self.size
        

if __name__ == "__main__":
    circularDeque = MyCircularDeque(3)      # 设置容量大小为3
    print(circularDeque.insertLast(1))		# 返回 true
    print(circularDeque.insertLast(2))		# 返回 true
    print(circularDeque.insertFront(3))		# 返回 true
    print(circularDeque.insertFront(4))		# 已经满了，返回 false
    print(circularDeque.getRear()) 			# 返回 2
    print(circularDeque.isFull())			# 返回 true
    print(circularDeque.deleteLast())		# 返回 true
    print(circularDeque.insertFront(4))		# 返回 true
    print(circularDeque.getFront())			# 返回 4
