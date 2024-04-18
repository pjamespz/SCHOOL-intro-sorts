import sorting 
import random
import time
import pandas as pd

names = ["MergeSort", "QuickSort", "InsertionSort", "ShellSort1", "ShellSort2", "BucketSort", "RadixSort", "BinaryInsertionSort"]

sorter = [None] * 8
sorter[0] = sorting.MergeSort()
sorter[1] = sorting.QuickSort()
sorter[2] = sorting.InsertionSort()
sorter[3] = sorting.ShellSort([7,3,1])
sorter[4] = sorting.ShellSort([1000,100,10,1])
sorter[5] = sorting.BucketSort(1000)
sorter[6] = sorting.RadixSort()
sorter[7] = sorting.BinaryInsertionSort()


DATA_SIZE = 500
NUM_EXP = 5
data = []

# Verification that sorting works
def verify(data, test_data, index):
    for i in range(DATA_SIZE):
        if test_data[i] != data[i]:
            print(names[index], "Incorrect Sorting!")
            exit
    print(names[index], "Successfully Sorted!")

for i in range(DATA_SIZE):
    data.append(random.randint(0,1000))
    
data_save = data.copy()
test_data = sorted(data)

for i in range(len(sorter)):
    data = data_save.copy()
    sorter[i].sort(data)
    verify(data,test_data,i)

DATA = [1000, 2000, 4000, 8000, 16000]
NUM_RUNS = 5
uniform_results = []
almost_sorted_results = []


# Uniformly Distributed Test Data
for t in DATA:
    for i in range(NUM_RUNS):
        random.seed(random.randint(0,500))
        data = []
        for i in range(t):
            data.append(random.randint(0,1000))

        for i in range(len(sorter)):
            data = data_save.copy()
            start_time = time.perf_counter()
            sorter[i].sort(data)
            end_time = time.perf_counter()
            sorter[i].time = end_time - start_time
            uniform_results.append({'Algorithm': names[i], 'Data Size': t, 'Runtime': sorter[i].time, 'Theoretical Big-O': 0})

uniform_results_df = pd.DataFrame(uniform_results)
uniform_results_df.to_csv('uniform_results.csv', index=False)

