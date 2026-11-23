import pandas as pd
import numpy as np

# Create a Series containing 10 random numbers
series = pd.Series(np.random.randint(1, 101, 10))

print("Original Series:")
print(series)

# Indexing
print("\nElement at index 3:")
print(series[3])

print("\nFirst five elements:")
print(series[:5])

# Filtering
print("\nNumbers greater than 50:")
print(series[series > 50])

# Statistical operations
print("\nStatistical Operations:")
print("Mean   :", series.mean())
print("Median :", series.median())
print("Minimum:", series.min())
print("Maximum:", series.max())