from Disk import *
from typing import List

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, val: int):
        if not self.top:
            self.top = Disk(val)
        else:
            new_top = Disk(val, self.top)
            self.top = new_top
        return self.top.val
    
    def pop(self):
        if self.top:
            num = self.top.val
            new_top = self.top.next
            self.top.next = None
            self.top = new_top
            return num
        return -1
    
    def stackToList(self) -> List[int]:
        result = []
        current_disk = self.top

        while current_disk:
            result.append(current_disk.val)
            current_disk = current_disk.next
        
        return result