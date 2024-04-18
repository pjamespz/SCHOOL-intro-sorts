import sorting 
import random
import time

'''
The first part of this code will verify functional correctness of all sorting algorithms.
Then, the code will time 
'''

random.seed(260)

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

for i in range(DATA_SIZE):
    data.append(random.randint(0,1000))
    
data_save = data.copy()
test_data = sorted(data)

def verify(data, test_data, index):
    for i in range(DATA_SIZE):
        if test_data[i] != data[i]:
            print(names[index], "Incorrect Sorting!")
            exit
    print(names[index], "Successfully Sorted!")

for i in range(len(sorter)):
    data = data_save.copy()
    sorter[i].sort(data)
    verify(data,test_data,i)


for j in range(NUM_EXP):
    print()
    DATA_SIZE = DATA_SIZE * 2
    print("DATA_SIZE:", DATA_SIZE)
    data = []
    for i in range(DATA_SIZE):
        data.append(random.randint(0,1000))
       
    data_save = data.copy()
    test_data = sorted(data)

    for i in range(len(sorter)):

        data = data_save.copy()
        start_time = time.perf_counter()
        sorter[i].sort(data)
        end_time = time.perf_counter()
        sorter[i].time = end_time - start_time

    for i in range(len(sorter)):
        print(names[i], sorter[i].time)






