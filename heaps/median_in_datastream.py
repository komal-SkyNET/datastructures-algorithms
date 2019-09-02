   
from collections import deque

def l_index(parent):
    return 2*parent+1
def r_index(parent):
    return 2*parent+2

def parent(data, i):
    return data[(i-1)/2]

def left(data, i):
    return data[2*i+1]

def right(data, i):
    if 2*i+2 > len(data)-1:
        return left(data, i)
    else:
        return data[2*i+2]

def swap(data, i, k):
    t = data[i]
    data[i] = data[k]
    data[k] = t

class MinHeap:
    
    def __init__(self):
        self.data = deque([])
    
    def insert(self,k):
        self.data.append(k)
        self.min_heapify()
    
    def min_heapify(self):
        i = len(self.data) - 1
        while parent(self.data, i) > self.data[i] and i>0 :
            swap(self.data, i, (i-1)/2)
            i = (i-1)/2
            
    def pop_min(self):
        if len(self.data)>1:
            result = self.data[0]
            self.data[0] = self.data.pop()
            i = 0
            while l_index(i) < len(self.data) and (self.data[i] > left(self.data, i) or self.data[i] > right(self.data, i)):
                if left(self.data, i) > right(self.data, i):
                    swap(self.data, i, r_index(i))
                    i = r_index(i)
                else:
                    swap(self.data, i, l_index(i))
                    i = l_index(i)
            return result
        else:
            return self.data.pop()
        
    def peek(self):
        return self.data[0]

    def __len__(self):
        return len(self.data)
        


class MaxHeap:
    
    def __init__(self):
        self.data = deque([])
    
    def insert(self,k):
        self.data.append(k)
        self.max_heapify()
    
    def max_heapify(self):
        i = len(self.data) - 1
        while parent(self.data, i) < self.data[i] and i>0 :
            swap(self.data, i, (i-1)/2)
            i = (i-1)/2
            
    def pop_max(self):
        if len(self.data)>1:
            result = self.data[0]
            self.data[0] = self.data.pop()
            i = 0
            while l_index(i) < len(self.data) and (self.data[i] < left(self.data, i) or self.data[i] < right(self.data, i)):
                if left(self.data, i) < right(self.data, i):
                    swap(self.data, i, r_index(i))
                    i = r_index(i)
                else:
                    swap(self.data, i, l_index(i))
                    i = l_index(i)
            return result
        else:
            return self.data.pop()
    
    def peek(self):
        return self.data[0]
    
    def __len__(self):
        return len(self.data)

        
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = MaxHeap()
        self.min_heap = MinHeap()
        
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.max_heap) == 0 and len(self.min_heap) == 0:
            self.max_heap.insert(num)
        elif self.max_heap.peek() > num:
            self.max_heap.insert(num)
        else:
            self.min_heap.insert(num)
        
        if abs(len(self.max_heap) - len(self.min_heap))>1:
            if len(self.max_heap) > len(self.min_heap):
                self.min_heap.insert(self.max_heap.pop_max())
            else:
                self.max_heap.insert(self.min_heap.pop_min())
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
            return (self.max_heap.peek() + self.min_heap.peek())/2.0
        elif len(self.max_heap) > len(self.min_heap):
            return self.max_heap.peek()
        else:
            return self.min_heap.peek()


test = MedianFinder()

test.addNum(1)
test.addNum(2)
print test.findMedian()
test.addNum(3)
print test.max_heap.data
print test.min_heap.data
print test.findMedian()