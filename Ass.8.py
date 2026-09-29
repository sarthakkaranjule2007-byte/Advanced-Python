# Program to read a file, count lines, and extract first two lines

# Open the input file in read mode
with open("input.txt", "r") as file:
    lines = file.readlines()

# Count the total number of lines
line_count = len(lines)

print("Total number of lines:", line_count)

# Extract the first two lines
first_two_lines = lines[:2]

# Write the extracted lines into a new file
with open("output.txt", "w") as file:
    file.writelines(first_two_lines)

print("First two lines have been written to output.txt")