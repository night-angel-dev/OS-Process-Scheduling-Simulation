# dont mind this, i just wanted to test if my code actually works since we haven't populated the other ones yet

from pathlib import Path
import data_gen


def test_data_gen():

    test_csv_path = Path("tests") / "test_processes.csv"

    num_test_jobs = 10
    data_gen.gen_jobs(filename=str(test_csv_path), num_processes=num_test_jobs)

    assert test_csv_path.exists(), f"Error: {test_csv_path} was not created"

    jobs = data_gen.load_jobs(filename=str(test_csv_path))

    assert len(jobs) == num_test_jobs, f"Expected {num_test_jobs} jobs, got {len(jobs)}"

    print(f"Loaded {len(jobs)} instances")

    sample_job = jobs[0]
    print("\nResults:")
    print(f"PID          : {sample_job.pid}")
    print(f"CPU Cycles   : {sample_job.cpu_cycles:,}")
    print(f"Memory (MB)  : {sample_job.memory_bytes:,}")
    print(f"Arrival Time : {sample_job.arrival_time}")

    if test_csv_path.exists():
        test_csv_path.unlink()
        print("\nClean up completed")


if __name__ == "__main__":
    test_data_gen()
