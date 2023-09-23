from queue import PriorityQueue, Queue
from datetime import datetime

class Patient:
    def __init__(self, name, treatment_time, urgency, arrival_time):
        self.name = name
        self.treatment_time = treatment_time
        self.urgency = urgency
        self.arrival_time = self.parse_arrival_time(arrival_time)

    def parse_arrival_time(self, arrival_time):
        time_obj = datetime.strptime(arrival_time, "%H:%M")
        return time_obj.hour * 60 + time_obj.minute

def fcfs_scheduling(patients):
    current_time = 0
    for patient in patients:
        current_time = max(current_time, patient.arrival_time)
        start_time = current_time
        end_time = start_time + patient.treatment_time
        print(f"Patient {patient.name}: Start Time = {start_time}, End Time = {end_time}")
        current_time = end_time

def sjf_scheduling(patients):
    patients.sort(key=lambda x: x.treatment_time)
    current_time = 0
    for patient in patients:
        current_time = max(current_time, patient.arrival_time)
        start_time = current_time
        end_time = start_time + patient.treatment_time
        print(f"Patient {patient.name}: Start Time = {start_time}, End Time = {end_time}")
        current_time = end_time

def ps_scheduling(patients):
    patients.sort(key=lambda x: x.urgency, reverse=True)
    current_time = 0
    for patient in patients:
        current_time = max(current_time, patient.arrival_time)
        start_time = current_time
        end_time = start_time + patient.treatment_time
        print(f"Patient {patient.name}: Start Time = {start_time}, End Time = {end_time}")
        current_time = end_time

def rr_scheduling(patients, time_quantum):
    current_time = 0
    queue = Queue()
    for patient in patients:
        queue.put(patient)

    while not queue.empty():
        patient = queue.get()
        current_time = max(current_time, patient.arrival_time)
        start_time = current_time
        if patient.treatment_time <= time_quantum:
            end_time = start_time + patient.treatment_time
            print(f"Patient {patient.name}: Start Time = {start_time}, End Time = {end_time}")
            current_time = end_time
        else:
            end_time = start_time + time_quantum
            print(f"Patient {patient.name}: Start Time = {start_time}, End Time = {end_time} (Partial)")
            current_time = end_time
            patient.treatment_time -= time_quantum
            queue.put(patient)

# Create patient objects
patients = [
    Patient("A", 30, 3, "00:00"),
    Patient("B", 20, 5, "00:10"),
    Patient("C", 40, 2, "00:15"),
    Patient("D", 15, 4, "00:20")
]

print("FCFS Scheduling:")
fcfs_scheduling(patients)
print("\nSJF Scheduling:")
sjf_scheduling(patients)
print("\nPriority Scheduling:")
ps_scheduling(patients)
print("\nRound Robin Scheduling (Time Quantum = 10):")
rr_scheduling(patients, 10)
