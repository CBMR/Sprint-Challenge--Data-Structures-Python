class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    self.current += 1
    if self.current == self.capacity:
        self.current = 0


  def get(self):
    if self == None:
        return self.storage
    else:
        remove_all_nones = [i for i in self.storage if i != None]
        return remove_all_nones