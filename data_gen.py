"""
data_gen.py - generates the jobs for process scheduling

"""

import csv
import random
from typing import List
from process import Process
import config


def gen_jobs(
    filename: str = config.DEFAULT_CSV_FILENAME,
    num_processes: int = config.NUM_PROCESSES,
) -> None:
    """
    Generates the populated csv with process burst times and memory requirements
    """
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["pid", "cpu_cycles", "memory_bytes", "arrival_time"])

        for pid in range(1, num_processes + 1):
            cpu_cycles = random.randint(config.MIN_BURST, config.MAX_BURST)
            memory_mb = random.randint(config.MIN_MEM_MB, config.MAX_MEM_MB)
            # not sure if this is correct for arrival time
            arrival_time = random.randint(0, 100)
            writer.writerow([pid, cpu_cycles, memory_mb, arrival_time])


def load_jobs(filename: str = config.DEFAULT_CSV_FILENAME) -> List[Process]:
    """
    Reads the genned csv from above and instantiates that Process obj sorted by arrival time
    """
    processes = []
    with open(filename, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            p = Process(
                pid=int(row["pid"]),
                cpu_cycles=int(row["cpu_cycles"]),
                memory_bytes=int(row["memory_bytes"]),
                arrival_time=int(row["arrival_time"]),
            )
            processes.append(p)

    processes.sort(
        key=lambda proc: proc.arrival_time if proc.arrival_time is not None else 0
    )
    return processes
