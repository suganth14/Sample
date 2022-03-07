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

start = time.perf_counter()

Threads = []
for i in range(len(inpu)):
    t = threading.Thread(target=func, args=[inpu[i]])
    t.start()
    Threads.append(t)

for i in range(len(inpu)):
    Threads[i].join()

end = time.perf_counter()
print(f'{end - start} seconds')

