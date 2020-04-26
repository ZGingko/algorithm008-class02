class BinaryHeap:
    d = 2
    def __init__(self, capacity):
        self.heap = []
        self.__capacity = capacity

    def isEmpty(self):
        return len(self.heap) == 0

    def isFull(self):
        return len(self.heap) == self.__capacity

    def __parent(self,i):
        return (i - 1)//BinaryHeap.d

    def __kthChild(self,i,k):
        return BinaryHeap.d*i + k
    
    def insert(self,item):
        """
        Inserts new element in to heap
        Complexity:O(logN)
        As worst case scenario, we need to traverse till the root 
        """
        if self.isFull():
            raise Exception("the heap is full!")
        self.heap.append(item)
        self.__heapifyUp(len(self.heap)-1)
        

    def delete(self,index):
        """
        Deletes element at index 
        Complexity:O(logN)
        """
        if self.isEmpty():
            raise Exception("the heap is empty!")
        maxElement = self.heap[index]
        self.heap[index] = self.heap.pop()
        self.__heapifyDown(index)
        return maxElement


    def __heapifyUp(self,i):
        insertValue = self.heap[i]
        while i>0 and insertValue > self.heap[self.__parent(i)]:
            self.heap[i] = self.heap[self.__parent(i)]
            i = self.__parent(i)
        self.heap[i] = insertValue

    def __heapifyDown(self,i):
        child = 0
        temp = self.heap[i]
        while self.__kthChild(i,1)<len(self.heap):
            child = self.__maxChild(i)
            if temp >= self.heap[child]:
                break
            self.heap[i] = self.heap[child]
            i = child
        self.heap[i] = temp


    def __maxChild(self,i):
        leftChild = self.__kthChild(i,1)
        rightChild = self.__kthChild(i,2)
        return leftChild if self.heap[leftChild]>self.heap[rightChild] else rightChild

    def printHeap(self):
        print("nHeap = ", end=" ")
        for i in range(len(self.heap)):
            print(self.heap[i],end = " ")
        print()

    def findMax(self):
        if self.isEmpty():
            raise Exception('the heap is empty!')
        return self.heap[0]

    

if __name__ == "__main__":
    maxHeap = BinaryHeap(10)
    maxHeap.insert(10)
    maxHeap.insert(4)
    maxHeap.insert(9)
    maxHeap.insert(1)
    maxHeap.insert(7)
    maxHeap.insert(5)
    maxHeap.insert(3)
    maxHeap.printHeap()
    maxHeap.delete(5)
    maxHeap.printHeap()
    maxHeap.delete(2)
    maxHeap.printHeap()