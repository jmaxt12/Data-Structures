class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)# I need to bubble up here

  def delete(self):
    if len(self.storage) > 1:
      self._swap(0, len(self.storage) - 1)
      max = self.storage.pop()
      self._sift_down(0)
    elif len(self.storage) == 1:
      max = self.storage.pop()
    else:
      return False
    return max

  def get_max(self):
    if self.storage:
      return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent = (index - 1)//2
    if index <= 0:
      return
    elif self.storage[index] > self.storage[parent]:
      self._swap(index, parent)
      self._bubble_up(parent)


  def _sift_down(self, index):
    left = index * 2 + 1
    right = index * 2 + 2
    largest = index
    if len(self.storage) > left and self.storage[largest] < self.storage[left]:
      largest = left
    if len(self.storage) > right and self.storage[largest] < self.storage[right]:
      largest = right

    if largest != index:
      self._swap(index, largest)
      self._sift_down(largest)

  def _swap(self, i, j):
    self.storage[i], self.storage[j] = self.storage[j], self.storage[i]
'''
  * `insert` adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
  * `delete` removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed. 
  * `get_max` returns the maximum value in the heap _in constant time_.
  * `get_size` returns the number of elements stored in the heap.
  * `_bubble_up` moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.
  * `_sift_down` grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.
'''