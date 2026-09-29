import csv
import json

# Open the CSV file
with open("input.csv", "r", newline="") as csv_file:
    reader = csv.DictReader(csv_file)

    # Convert CSV data into a list of dictionaries
    data = list(reader)

# Write the data into a JSON file
with open("output.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON.")
print("Output stored in output.json")