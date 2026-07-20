"""
config.py - Global parameteres for the simulator
"""

NUM_PROCESSES: int = 250
NUM_PROCESSORS: int = 6
DEFAULT_CSV_FILENAME: str = "processes.csv"

# 10 * 10^6 to 10^12 cycles
MIN_BURST: int = 10 * (10**6)
MAX_BURST: int = 10 * (10**12)

# 1MB to 16GB
MIN_MEM_MB: int = 1
MAX_MEM_MB: int = 16 * 1024

# for parts 2 & 3, you can ignore this for now ig
SLOW_CORE_SPEED_GHZ: int
FAST_CORE_SPEED_GHZ: int
SLOW_CORE_RAM_MB: int
FAST_CORE_RAM_MB: int

# for part 4
LOOKAHEAD_WINDOW_SIZE: int = 5

TIME_QUANTUM: int = 4
