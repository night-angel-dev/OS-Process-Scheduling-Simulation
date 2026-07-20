"""
process.py - The process class file. Represents a single process in the overall system. 
Essentially a data container for information, but does not act within the system.

"""


class Process:
    
    
    
    
    
    def __init__(self, pid: int, cpu_cycles: int, memory_bytes: int, arrival_time: int = None):
        """
        Initialization for a new process. Enforces specific data types of parameters.
        
        @param pid - Int Process Identifier 
        @param cpu_cycles - Int Total cpu cycles needed to finish executing. Equivalent to burst time. 
        @param memory_bytes - Int The memory requirements of the process. Needed when deciding to assigning to a processor with limited memory. 
        @param arrival_time - Int Time when process arrives to system. Not sure how to apply this yet so default value is None.  
    
        """
        
        # Process Identifier
        self.pid = pid
        
        # resource requirements/constraints
        self.cpu_cycles = cpu_cycles
        self.memory_bytes = memory_bytes
        self.remaining_cycles = cpu_cycles # Initally equal to cpu_cycles
        
        # time information
        self.arrival_time = arrival_time
        self.start_time = None # Reason why this does not start at 0 is because that can be a start time
        self.finished_time = None
        
        # Calculated information, stats file does the calculation not this file
        self.waiting_time = None
        self.turnAround_time = None
        
    
    
    def is_complete(self) -> bool:
        
        """
        Checks if process has finished executing.
        
        @return bool - True if remaining_cycles <= 0. False otherwise.
        
        """
        return self.remaining_cycles <= 0
    
        
    def has_started(self) -> bool:
        """
        Checks if the process has ever begun executing.
        
        @return bool - True if start_time is not None. False otherwise.
        """
        
        return self.start_time != None
        
    


    
    
    
# Quick tests
if __name__ == "__main__":
    
    print("Test 1: Create a Process")
    p1 = Process(1, 100, 512, 0 )
    print(f"Created PID: {p1.pid}, (cycles required/burst time = {p1.cpu_cycles}, memory requirements = {p1.memory_bytes})")
    print(f"Arrival time: {p1.arrival_time}, remaining cycles: {p1.remaining_cycles}")
    print(f"Has started? {p1.has_started()}, should be false")
    print(f"Is complete? {p1.is_complete()}, should be false\n")
    
    
    
    print("Test 2: ")
    
    pass