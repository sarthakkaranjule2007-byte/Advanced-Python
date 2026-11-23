import gc
import time
import tracemalloc

# Class to create circular references
class Node:
    def __init__(self, name):
        self.name = name
        self.reference = None


# Function to create circular reference objects
def create_circular_objects(count):
    for i in range(count):
        obj1 = Node(f"Object A{i}")
        obj2 = Node(f"Object B{i}")

        # Create circular references
        obj1.reference = obj2
        obj2.reference = obj1


# Function to display memory usage
def display_memory(label):
    current, peak = tracemalloc.get_traced_memory()
    print(f"{label}")
    print(f"Current Memory: {current / 1024:.2f} KB")
    print(f"Peak Memory: {peak / 1024:.2f} KB")


# Main program
tracemalloc.start()

print("Initial Garbage Collection Status:", gc.isenabled())

# Disable automatic garbage collection
gc.disable()
print("\nAutomatic Garbage Collection Disabled")

# Create circular reference objects
create_circular_objects(10000)

display_memory("\nBefore Manual Garbage Collection:")

# Check garbage collector statistics
print("Garbage Collection Counts:", gc.get_count())

# Perform manual garbage collection
start_time = time.perf_counter()
collected = gc.collect()
end_time = time.perf_counter()

print("\nManual Garbage Collection Results")
print("Objects Collected:", collected)
print("Time Taken:", end_time - start_time, "seconds")

display_memory("\nAfter Manual Garbage Collection:")

# Enable automatic garbage collection
gc.enable()
print("\nAutomatic Garbage Collection Enabled:", gc.isenabled())

# Create objects with automatic GC enabled
create_circular_objects(10000)

display_memory("\nAfter Creating Objects with Automatic GC Enabled:")

# Allow a manual collection for final comparison
start_time = time.perf_counter()
collected = gc.collect()
end_time = time.perf_counter()

print("\nFinal Garbage Collection")
print("Objects Collected:", collected)
print("Time Taken:", end_time - start_time, "seconds")

display_memory("\nFinal Memory Usage:")

tracemalloc.stop()