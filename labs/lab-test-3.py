#Name: ABdul AIdil Shah bin Ajibir, Class: C02

import csv
def calculate_average_height(filename):
    f = open(filename, "r", newline="")
    reader = csv.reader(f)

    next(reader)
    total_height = 0
    count = 0

    for row in reader:
        print(row)
        total_height = total_height + float(row[1])
        count = count + 1
    average = total_height / count
    f.close()
    return average

print("Average height:", calculate_average_height("labs/bmi.csv"))

def add_data(filename):
    gender = input("Enter gender: ")
    height = input("Enter height: ")
    weight = input("Enter weight: ")
    bmi = input("Enter bmi: ")

    data = open(filename, "a+", newline="")
    writer = csv.writer(data)
    writer.writerow([gender, height, weight, bmi])
    data.close()

    print("\nUpdated file content:")

    data = open(filename, "r", newline="")
    reader = csv.reader(data)

    for row in reader:
        print(row)

    data.close()

add_data("labs/bmi.csv")
