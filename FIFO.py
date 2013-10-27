import sys

def FIFO_scheduler(process_queue, cpu_list, time_for_context_switch):
# While there are still more values in the process_queue, continue scheduling them
    time = 0

    #Initialize times
    min_turnaround_time = sys.maxsize
    avg_turnaround_time = sys.maxsize
    max_turnaround_time = sys.maxsize

    min_init_wait_time = sys.minsize
    avg_init_wait_time = sys.minsize
    max_init_wait_time = sys.minsize

    min_total_wait_time = 0
    avg_total_wait_time = 0
    max_total_wait_time = 0

    while process_queue.empty() is False:
        process = process_queue.get()
        print("time %(time)dms Process %(pid)d created (requires %(burst)dms CPU time)" % {'time': time, 'pid': process.process_id, 'burst': process.cpu_burst_time})

        #Update the wait time for this procedure
        process.total_wait_time = process.init_wait_time = time


