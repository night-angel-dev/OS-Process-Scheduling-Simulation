"""
ready_queue.py - Class file for ready queue needed in the process scheduling system. Contains processes that are ready to be assigned to a processor.
The scheduler will sort/reorder this queue based on the scheduling algorithm.

"""

from collections import deque 


class ReadyQueue:
    
    def __init__(self):
        """
        Initializes an empty ready queue. 
        Benefits over list: O(1) appending and popleft operations.
        We shoud know how to sort a queue. 
        """
        
        self.queue = deque()
        
        pass
    
    def add_process(self, process):
        
        """
        Add a process to the ready queue.
        
        @param process - The process being added.
        """
        
        # safety chceck
        if process is None:
            return None
        
        self.queue.append(process)
    
        pass
    
    
    def get_next(self):
        
        """
        Retrieves and removes the next process from the ready queue.
        
        @return process - The next process
        @return None - None if empty
        
        """
        
        if self.queue.is_empty():
            return None
        
        return self.queue.popleft()
        
        pass
    
    
    def peek(self, index = 0):
        """
        Looks at next process(s) without removing it. 
        
        @return process - The next process
        @return None - None if empty
        """
        
        if self.queue.is_empty():
            return None
        
        
        return self.queue[index]
                
        
        pass
    
    
    def is_empty(self) -> bool:
        
        """
        Checks if ready queue is empty.
        
        @return bool - True if empty. False otherwise.
        """
        
        return len(self.queue) == 0
        
        
        pass
    
    
    def remove_process(self, pid) -> bool:
        """
        Removes a process fromn ready_queue by its PID.
        
        @return bool - True if process is found. False otherwise.
        """
        
        i = 0
        
        for process in self.queue:
            
            if process.pid == pid:
                
                temp = list(self.queue)
                temp.pop(i)
                self.queue = deque(temp)
                
                return True
            
            i += 1 
        return False
        
        pass
    
    def size(self) -> int:
        """
        Get the size/number of processes in ready queue.
        
        @return int - Queue length
        """
        
        return len(self.queue)
        
        pass
    
    
    def get_all(self):
        """
        Get all processes from ready queue for sorting purposes.
        
        @return list - List of all processes in ready queue.
        """
        
        return list(self.queue) 
        
    

    
    
if __name__ == "__main__":
    
    
    pass