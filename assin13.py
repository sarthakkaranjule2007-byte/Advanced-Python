import threading
import time

# Task 1: Print numbers
def print_numbers():
    for i in range(1, 6):
        print(f"Thread 1 - Number: {i}")
        time.sleep(1)

# Task 2: Print alphabets
def print_alphabets():
    for ch in ['A', 'B', 'C', 'D', 'E']:
        print(f"Thread 2 - Alphabet: {ch}")
        time.sleep(1)

# Task 3: Display messages
def display_messages():
    messages = ["Hello", "Welcome", "Python", "Multithreading", "Complete"]
    for msg in messages:
        print(f"Thread 3 - Message: {msg}")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_alphabets)
t3 = threading.Thread(target=display_messages)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()

print("\nAll threads have completed execution.")