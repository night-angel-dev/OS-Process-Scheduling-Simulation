"""
processor.py - Processor/core class file. Represents a CPU/Processor/Core that executes processes. 
The processor is what deecrements the cycles or does the execution of a process.

"""

from process import Process

class Processor:
    
    
    
    def __init__(self, processor_ID: str, speed: int = 1, memory_capacity: int):
        """
        Initialize proccessor core/CPU.
        
        @Param processor_ID str - Identifier of core (i.e., P_A or P_B)
        @Param speed int - Cycles executed within one time unit, default should be 1 for now. 
        @Param memeory_capacity int - Maximum memory this processor can handle. Processor should not handle a task that demands more memory than the processor can handle.
        """
        
        self.processor_ID = processor_ID
        
        # current work and availability 
        self.current_process = None # Initially should be none
        self.is_available = True # Initally True 
        
        # Specs, needed for parts 2 and 3 
        self.speed = speed
        self.memory_capacity = memory_capacity
        
        
        
        pass
    
    
    
    def assign_process(self, process: Process):
        """
        Assigns a process for the core/processor to execute. 
        
        @Param process - Process being assigned
        @Return boolean - For confirmation. True if success. False otherwise. 
        """
        
        # busy
        if self.is_available == False:
            return False
        
        # Check memeory constraints
        if self.can_accept(process) == False:
            return False
        
        # Assign process
        self.current_process = process
        self.is_available = False
        
        # Record start time if this is the first time executing
        if process.has_started() == False:
            
            process.start_time = None # seen and checked in execute cycles
        
        return True
        
        
        pass
    
    
    def execute_cycles(self, current_time):
        """
        Executes one time units worth of work on current process. 
        Deecrements remaining_cycles by speed. Function should be not responsible for main execution loop.
        The simulator holds that responsibility, along with deciding when to check for preemptions. 
        scheduler is responsible for time quantum usage and preemption decisions.
        
        @param current_time - time used time related calculations
        
        @return Process - If process has finished 
        @return None - If still running or there is no process
        """
        
        # If there is no process assigned or the process is already complete
        
        if self.current_process == None:
            return None
        
        if self.current_process.is_complete():
            self.release_current_process()
            return None
        
        # Set start time to current time on first execution
        if self.current_process.has_started() == None:
            self.current_process.start_time == current_time
        
        # Now we can execute one unit time of work
        self.current_process.remaining_cycles -= self.speed
        
        
        # check if process completed from time unit of work
        if self.current_process.is_complete():
            
            # Record completion time
            self.current_process.finished_time = current_time
            
            # Clean up
            completed = self.current_process
            self.reset()
            
            return completed
        
        
        # If we are here this mean the process still has work remaing
        return None
        
        
        pass
    
    
    def is_idle(self) -> bool:
        
        """
        Checks if processor is free/idle.
        
        @return boolean - True if no assigned process. False otherwise. 
        """
        return self.current_process == None

        
        
        pass
    
    
    def can_accept(self, process) -> bool:
        """
        Checks if a processor can even accept a process based on memory requirements.
        
        @param process - The process we are checking
        @return boolean - True if process memory <= memory_capacity. False otherwise.
        """
        
        if process == None:
            return False
        
        return process.memory_bytes <= self.memory_capacity
                
        
        
        
        pass
    
    
    
    
    def reset(self):
        """
        Reset process to idle state.
        Clears current process and make processor available
        """
        
        self.current_process = None
        self.is_available = True
        
        pass
    
    
    def release_current_process(self):
        """
        Mainly for round robin.
        Releases the current process, needed for preemption.
        Returns the process that it can be put back into ready queue.
        
        @return process - The released process
        @return None - if there was no process
        
        """
        
        if self.current_process == None:
            return None
        
        
        released = self.current_process
        self.reset()
        
        return released
        
        
        pass
    
    
    
    
    
if __name__ == "__main__":
    
    
    
    
    pass