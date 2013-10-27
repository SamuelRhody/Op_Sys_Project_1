import random
import queue    #For FIFO queue
import heapq    #For priority queues

#Global time variable
time = 0

class Process:
    def __init__(self, process_id, cpu_burst_time):
        self.process_id = process_id
        self.cpu_burst_time = cpu_burst_time
        self.wait_time = 0

    #Function to make the process continually wait
    def wait(self):
        self.wait_time += 1

    def get_burst_time(self):
        return self.cpu_burst_time

    def get_process_id(self):
        return self.process_id

    def __repr__(self):
        return self.process_id + " " + self.cpu_burst_time

class CPU:
    def __init__(self, name):
        self.name = name
        self.current_running_process = None
    # end init definition

    def add_process(self, process):
        if( self.current_running_process is None ):
            self.current_running_process = process
            return True
        else:
            return False

    def has_running_process(self):
        return (process is not None)

    def __repr__(self):
        return self.name


def schedule_process(next_process, cpu_list):
    global time #make time global throughout
    process_running = False
    while(process_running is False):
        for cpu in cpu_list:
            if(cpu.add_process(next_process) is True):
                process_running = True
                break
            #Increment time upon trying to add a process
            time += 1
            next_process.wait() #If could not run, then increment waiting time


def FCFS_scheduler(process_queue, cpu_list):
    while(process_queue.empty() is False):
        next_process = process_queue.get()
        schedule_process(next_process, cpu_list)
        process_queue.task_done()

def priority_scheduler(process_queue, cpu_list):
    priority_queue = []
    for process in process_queue:
        heappush(priority_queue, process)

num_cpus = 4
num_processes = 20
cpus = list()
#Create the n CPUs
for i in range(0, num_cpus):
    #Initialize CPUs with sequential name
    cpu_name = chr(i + 65)
    #cpu_burst = random.randrange(50, 400)
    cpus.append(CPU(cpu_name) )

process_queue = queue.Queue(num_processes)
#Create the processes
for i in range(0, num_processes):
    #Initialize processes with sequential pid and random cpu burst
    cpu_burst = random.randrange(50, 400)
    process_queue.put(Process(i, cpu_burst), False)

FCFS_scheduler(process_queue, cpus)
