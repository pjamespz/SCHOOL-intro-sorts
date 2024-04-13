import sorting 
import random
import time

'''
The first part of this code will verify functional correctness of all sorting algorithms.
Then, the code will time 
'''

random.seed(260)

names = ["MergeSort", "QuickSort", "InsertionSort", "ShellSort1", "ShellSort2", "BucketSort", "RadixSort"]

sorter = [None]*7
sorter[0] = sorting.MergeSort()
sorter[1] = sorting.QuickSort()
sorter[2] = sorting.InsertionSort()
sorter[3] = sorting.ShellSort([7,3,1])
sorter[4] = sorting.ShellSort([1000,100,10,1])
sorter[5] = sorting.BucketSort(1000)
sorter[6] = sorting.RadixSort()

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

# Please read all of the following before starting your implementation:
#
# Details about Gradescope submission:
#
# - You should not include anything outside of standard Python libraries.
# - Functions should be tested using Python 3.6+ on a Linux environment.
# - You must submit the requirements.py and the sorting.py files, along with any additional source files that you might create
# - The submission should either be the files themselves, or a zip file not containing any directories.
# - We have provided a project1_tests.py file that contains some simple test cases to give an idea of how we will be running your
#   code. Please use that file when testing your implementation.
#
# Finish the implementations of the following sorting algorithms:
# 
# - MergeSort
# - QuickSort
# - InsertionSort
# - ShellSort
# - BucketSort
# - RadixSort
#
# - Each algorithm is implemented as a class. The testing code can be seen above. 
