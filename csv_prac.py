import csv
import threading
import time

inpu = []


def func(value):
    with open('output.csv', 'a', newline='') as file:
        write = csv.writer(file, delimiter=' ')
        write.writerow([str(value**2)])
    file.close()


with open('input.csv', 'r', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in data:
        inpu.append(int(row[0]))
csvfile.close()

for val in inpu:
    func(val)
