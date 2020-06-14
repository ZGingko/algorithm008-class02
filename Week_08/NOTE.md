# 学习笔记
## 知识点总结
### 第16课 位运算
1. 指定位置的位运算  

> 1. 将 `x` 最右边的n位清零: `x & (~0 << n) `   
   `10110 & (11111111111111111111111111111111 << n) -> 10110 & (11111111111111111111111111111000)`
> 2. 获取 `x` 的第 `n` 位的值: `(x >> n) & 1`  
> `10110 >> 3 -> 10 & 1 -> 0`
> 3. 获取 `x` 的第 `n` 位的幂值: `x & (1 << n)`  
   `1 << n -> 1000 -> 10110 & 01000 -> 0000`  
   `1 << n -> 1000 -> 11110 & 01000 -> 1000`
> 4. 仅将第 `n` 位置为 `1`: `x | (1 << n)`
   `1 << n -> 1000 -> 10110 | 1000 -> 11110`
> 5. 仅将第 `n` 位置 `0`: `x & (~(1 << n))`
> 6. 将 `x` 最高位至第 `n` 位(含)清零: `x & ((1 << n) - 1)`
> 7. 将 `x` 第 `n` 位至第 `0` 位(含)清零: `x & (~((1 << n) - 1))`
> 8. 得到最低位的值: `x & 1`
> 9. 将最低位的 `1` 清 `0`: `x & (x - 1)` 

2. 位运算实战要点记录

> 1. 判断奇偶  
   `x % 2 == 1 -> (x & 1) == 1`, 奇数  
   `x % 2 == 0 -> (x & 1) == 0`, 偶数
> 2. `x >> 1 -> x / 2`  
   `mid = (left + right) / 2 -> mid = (left + right) >> 1`
> 3. `x = x & (x - 1)` 清零最低位的 `1`  // `10110 & 10101 -> 10100`
> 4. `x & -x` 得到最低位的 `1` // `10110 & 0..1011 -> 00` (负数的二进制为: 原码取反+1)
> 5. `x & ~x == 0`   

3. N皇后问题的位运算解法
   ```python
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return []
        
        def DFS(row, cols, xy_dif, xy_sum):
            if row >= n:
                self.result += 1
                return 
            
            bits = (~(cols|xy_dif|xy_sum)) & ((1 << n) - 1) # 得到当前所有的空位
            print("row:{}, cols:{}, xy_dif:{}, xy_sum:{}, bits:{}".format(bin(row), bin(cols), bin(xy_dif), bin(xy_sum), bin(bits)))
            
            while bits:
                p = bits & -bits # 取到最低位的1
                bits = bits & (bits - 1) # 表示在p位置上放入皇后
                DFS(row + 1, cols | p, (xy_dif | p) << 1, (xy_sum | p) >> 1)
                # 不需要revert cols, xy_dif, xy_sum
        
        self.result = 0
        DFS(0, 0, 0, 0)
        return self.result
   ```
### 第17课 布隆过滤器和LRU缓存
1. 布隆过滤器
   * 使用多个 哈希函数 要加入的值进行哈希运算，计算出多个哈希值，放到对应的多个槽
   * 布隆过滤器可能会误识别：
     * 例如数值 A 计算出的哈希值是 1,2，B 计算出的哈希值是 1,3。把 A 和 B 存进布隆过滤器
     * 现在有一个值 C，想判断是否存在。C 计算出的哈希值是 2,3，刚好 A、B 把 2,3 填充过了，此时就会误识别
   * 如果不存在，一定就是不存在
   * 布隆过滤器极其省空间，因为都是存 bit。一般用于基数很大的例如垃圾邮件识别等等。

2. LRU缓存
   * 最近最少使用的缓存
   * 淘汰策略是：给定一定长度的数组(链表)，访问、插入元素的时候，会把这个元素放到最前面，当长度不够的时候，会淘汰最后一个元素。

### 第18课 排序算法
1. 冒泡排序
   ```python
    def bubble_sort(alist):
        n = len(alist)
        for i in range(n-1):
            count = 0
            for j in range(0, n - 1 - i):
                if alist[j] > alist[j + 1]:
                    alist[j], alist[j + 1] = alist[j + 1], alist[j]
                    count += 1
            if count == 0:
                return
   ```
   > 稳定，时间复杂度：平均 $O(n^2)$, 最优 $O(n)$, 最差 $O(n^2)$, 空间复杂度：$O(1)$

2. 选择排序
   ```python
    n = len(alist)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist
   ```
   > 不稳定，时间复杂度：平均 $O(n^2)$, 最优 $O(n^2)$, 最差 $O(n^2)$, 空间复杂度：$O(1)$

3. 插入排序
   ```python
    def insertion_sort(alist):
        n = len(alist)
        for i in range(1, n):
            pre = i - 1
            cur = alist[i]
            while pre >= 0 and alist[pre] > cur:
                alist[pre+1] = alist[pre]
                pre -= 1
            alist[pre+1] = cur
        return alist
   ```
   > 稳定，时间复杂度：平均 $O(n^2)$, 最优 $O(n)$, 最差 $O(n^2)$, 空间复杂度：$O(1)$

4. 希尔排序
   ```python
    def shell_sort(alist):
        n = len(alist)
        gap = n // 2
        while gap > 0:
            # 与插入算法的区别就似乎gap步长
            for j in range(gap, n):
                i = j  # j = [gap, gap + 1, gap + 2, ..., n - 1]
                while i > 0:
                    if alist[i] < alist[i-gap]:
                        alist[i], alist[i-gap] = alist[i-gap], alist[i]
                        i -= gap
                    else:
                        return
            gap = gap // 2 # 缩短gap步长
   ```
   > 不稳定，时间复杂度：平均 $O(n^{1.3})$, 最优 $O(n)$, 最差 $O(n^2)$, 空间复杂度：$O(1)$

5. 归并排序
   ```python
    def merge_sort(alist):
        n = len(alist)
        if n <= 1:
            return alist
        mid = n // 2
        left = merge_sort(alist[:mid])
        right = merge_sort(alist[mid:0])
        left_pointer, right_pointer = 0, 0
        result = []
        while left_pointer < len(left) and right_pointer < len(right):
            if left[left_pointer] < right[right_pointer]:
                result.append(left[left_pointer])
                left_pointer += 1
            else:
                result.append(right[right_pointer])
                right_pointer += 1
        result += left[left_pointer:]
        result += right[right_pointer:]
        return result
   ```
   > 稳定，时间复杂度：平均 $O(n{log_2{n}})$, 最优 $O(n{log_2{n}})$, 最差 $O(n{log_2{n}})$, 空间复杂度：$O(n)$

6. 快速排序
   ```python
    def quick_sort(alist, first, last):
        if first >= last:
            return
        mid_value = alist[first]
        low = first
        high = last
        while low < high:
            # high往前移动，遇到比mid_value小的，交给low，并停止移动
            while low < high and alist[high] >= mid_value:
                high -= 1
            alist[low] = alist[high]

            # low往后移动，遇到比mid_value大的，交给high，并停止移动
            while low < high and alist[low] < mid_value:
                low += 1
            alist[high] = alist[low]
        # 退出循环时，low == high
        alist[low] = mid_value # alist[high] = mid_value
        quick_sort(alist, first, low-1)
        quick_sort(alist, low+1, last)
   ```
   > 不稳定，时间复杂度：平均 $O(n{log_2{n}})$, 最优 $O(n{log_2{n}})$, 最差 $O(n^2)$, 空间复杂度：$O(n{log_2{n}})$

7. 堆排序
   ```python
    import math
    
    def heapify(alist, i):
        left = 2*i + 1
        right = 2*i + 2
        largest = i
        if left < alist_len and alist[left] > alist[largest]:
            largest = left
        if right < alist_len and alist[right] > alist[largest]:
            largest = right
        
        if largest != i:
            alist[i], alist[largest] = alist[largest], alist[i]
            heapify(alist, largest)   
    
   
    def buildMaxHeap(alist):
       for i in range(math.floor(len(alist)/2), -1, -1):
           heapify(alist, i)

    def heap_sort(alist):
        global alist_len
        alist_len = len(alist)
        n = alist_len
        buildMaxHeap(alist)
        for i in range(n-1, 0, -1):
            alist[0], alist[i] = alist[i], alist[0]
            alist_len -= 1
            heapify(alist, 0)
        return alist
   ```
   > 不稳定，时间复杂度：平均 $O(n{log_2{n}})$, 最优 $O(n{log_2{n}})$, 最差 $O(n{log_2{n}})$, 空间复杂度：$O(1)$

8. 计数排序
    ```python
    def counting_sort(alist):
        max_value = max(alist)
        bucket_len = max_value + 1
        bucket = [0] * bucket_len
        sorted_index = 0
        n = len(alist)
        for i in range(n):
            if not bucket[alist[i]]:
                bucket[alist[i]] = 0
            bucket[alist[i]] += 1
        
        for j in range(bucket_len):
            while bucket[j] > 0:
                alist[sorted_index] = j
                sorted_index += 1
                bucket[j] -= 1
        return alist
    ```
    > 稳定，时间复杂度：平均 $O(n+k)$, 最优 $O(n+k)$, 最差 $O(n+k)$, 空间复杂度：$O(n+k)$

9. 桶排序
    ```python
    def bucket_sort(alist):
        min_num = min(alist)
        max_num = max(alist)

        bucket_range = (max_num - min_num) // len(alist) # 桶的大小
        count_list = [[] for i in range(len(alist) + 1)] # 桶数组

        for item in alist:
            count_list[(item-min_num)//bucket_range].append(item)
        alist.cleat()
        for item in count_list:
            for elem in sorted(item):
                alist.append(elem)
        return alist
    ```
    > 稳定，时间复杂度：平均 $O(n+k)$, 最优 $O(n)$, 最差 $O(n^2)$, 空间复杂度：$O(n+k)$

10. 基数排序
    ```python
    def radix_sort(alist):
        i = 0 # 初始为个位数排序
        n = 1 # 最小位数置为1（包含0）
        max_num = max(alist) # 获取数组中最大数
        while max_num > 10**n: # 获取最大数的位数
            n += 1
        while i < n:
            bucket = {} # 用字典构建桶
            for x in range(10):
                bucket.setdefault(x, []) # 将每个桶置为空
            for x in alist: # 对每一位数进行排序
                radix = int((x/(10**i)) % 10) # 得到每位的基数
                bucket[radix].append(x) # 将对应的数组元素加入到相应位基数的桶中
            j = 0
            for k in range(10):
                if len(bucket[k] != 0): # 若桶不为空
                    for y in bucket[k]: # 将桶中每个元素放回到数组中
                        alist[j] = y
                        j += 1
            i += 1
        return alist
    ```
    > 稳定，时间复杂度：平均 $O(n*k)$, 最优 $O(n*k)$, 最差 $O(n*k)$, 空间复杂度：$O(n+k)$