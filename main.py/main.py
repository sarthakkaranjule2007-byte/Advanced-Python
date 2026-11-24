import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Students scoring above 75:")

    for row in reader:
        if int(row["Marks"]) > 75:
            print(row["Name"], "_", row["Marks"])