import threading
import concurrent.futures
import time

start = time.perf_counter()

sq = []

i = -1
j = -1


def func(val):
    global i
    i += 1
    sq.append(val[i] ** 2)
    time.sleep(2)


def func1(val):
    global j
    j += 1
    time.sleep(2)
    return val[j] ** 2


# Threads = []
# for _ in range(10):
#     t = threading.Thread(target=func, args=[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
#     t.start()
#     Threads.append(t)
#
# for i in range(10):
#     Threads[i].join()

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(func, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f1.result())

end = time.perf_counter()
print(f'Finished in {end - start} seconds')
