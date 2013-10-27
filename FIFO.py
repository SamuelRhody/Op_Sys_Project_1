import sys

def FIFO_scheduler(process_queue, cpu_list, time_for_context_switch):
# While there are still more values in the process_queue, continue scheduling them
    time = 0

    min_turnaround_time = sys.maxsize
    avg_turnaround_time = sys.maxsize
    max_turnaround_time = sys.maxsize

    min_init_wait_time = sys.maxsize
    avg_init_wait_time = sys.maxsize
    max_init_wait_time = sys.maxsize

    min_total_wait_time = sys.maxsize
    avg_total_wait_time = sys.maxsize
    max_total_wait_time = sys.maxsize

    for process in process_queue:
        print("time %(time)dms Process %(pid)d created (requires %(burst)dms CPU time)" % {'time': time, 'pid': process.process_id, 'burst': process.cpu_burst_time})


