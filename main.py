import threading
import random

X = 1000
sync_X = 1000
num_adders = random.randint(1, 10)
num_subtractors = random.randint(1, 15)
print(f"Number of adders:{num_adders}")
print(f"Number of subtractors:{num_subtractors}\n")

adders = []
subtractors = []
sync_adders = []
sync_subtractors = []

adder_random_range = random.randint(100, 1000)
subtractor_random_range = random.randint(100, 1000)

print(f"adder_random_range:{adder_random_range}")
print(f"subtractor_random_range:{subtractor_random_range}\n")

def adder_process():
    global X
    for _ in range(adder_random_range):
        if X <= 1800:
            X += 1

def subtractor_process():
    global X
    for _ in range(subtractor_random_range):
        if X >= 0:
            X -= 1

lock = threading.Lock()

def sync_adder_process():
    global sync_X
    for _ in range(adder_random_range):
        with lock:
            if sync_X <= 1800:
                sync_X += 1

def sync_subtractor_process():
    global sync_X
    for _ in range(subtractor_random_range):
        with lock:
            if sync_X >= 0:
                sync_X -= 1

for _ in range(num_adders):
    adder_thread = threading.Thread(target=adder_process)
    adders.append(adder_thread)

for _ in range(num_subtractors):
    subtractor_thread = threading.Thread(target=subtractor_process)
    subtractors.append(subtractor_thread)

for adder_thread in adders:
    adder_thread.start()

for subtractor_thread in subtractors:
    subtractor_thread.start()

for adder_thread in adders:
    adder_thread.join()

for subtractor_thread in subtractors:
    subtractor_thread.join()

print(f"Without Synchronization - Final value of X: {X}")

for _ in range(num_adders):
    sync_adder_thread = threading.Thread(target=sync_adder_process)
    sync_adders.append(sync_adder_thread)

for _ in range(num_subtractors):
    sync_subtractor_thread = threading.Thread(target=sync_subtractor_process)
    sync_subtractors.append(sync_subtractor_thread)

for sync_adder_thread in sync_adders:
    sync_adder_thread.start()

for sync_subtractor_thread in sync_subtractors:
    sync_subtractor_thread.start()

for sync_adder_thread in sync_adders:
    sync_adder_thread.join()

for sync_subtractor_thread in sync_subtractors:
    sync_subtractor_thread.join()

print(f"With Synchronization - Final value of X: {sync_X}")
