import sorting 
import random
import time
import pandas as pd
import sys
import math

sys.setrecursionlimit(2000000000 ) #Let Quicksort cook
print("Recursion limit is:", sys.getrecursionlimit())
#generate almost-sorted swapmap function
def genSwapmap(n):
    numpairs = math.trunc(2*math.log(n))
    i = []
    j = []
    for iter in range(1,numpairs+1):
        idx1 = random.randint(0,n-1)
        idx2 = random.randint(0,n-1)
        if idx1 not in i and idx1 not in j and idx2 not in i and idx2 not in j:
            i.append(idx1)
            j.append(idx2)
    return i, j

''' Unused; == comparison is equivalent here, simpler, less prone to looping weirdness.
# Verification that sorting works
def verify(data, test_data, index):
        if test_data == data:
            print(names[index], "Sorted!")
        else:
            print(names[index], "Successfully Sorted!")
'''

### Initialization

names = ["MergeSort", "QuickSort", "InsertionSort", "ShellSort1", "ShellSort2", "BucketSort", "RadixSort", "CustomSort1", "MoMSort"]

sorter = [None] * 9
sorter[0] = sorting.MergeSort()
sorter[1] = sorting.QuickSort()
sorter[2] = sorting.InsertionSort()
sorter[3] = sorting.ShellSort([7,3,1])
sorter[4] = sorting.ShellSort([1000,100,10,1])
sorter[5] = sorting.BucketSort(1000)
sorter[6] = sorting.RadixSort()
sorter[7] = sorting.BinaryInsertionSort()
sorter[8] = sorting.MoMSort()

SIZES = [500, 1000, 2000, 4000, 8000] # Data sizes to iterate across
#NUM_EXP = 5 Redundant if looping using seed array.
SEEDS = random.sample(range(1,1000),4)
SEEDS.insert(0, 260)

data = []
uniform_results = []
almost_results = []
swap1 = []
swap2 = []

### Uniform loop beginning
for SIZE in SIZES:
    
    for SEED in SEEDS: #conduct a trial for every seed and algorithm at the current data size.
        random.seed(SEED)
        
        #create random data.
        data = []
        for i in range(SIZE):
            data.append(random.randint(0,1000))
        
        data_save = data.copy()
        test_data = sorted(data)

        for j in range(len(sorter)):
            data = data_save.copy()  # Reset data to its original unsorted state before sorting.
            start_time = time.perf_counter()
            sorter[j].sort(data)
            end_time = time.perf_counter()

            if test_data != data:
                print(names[j], SIZE, SEED,  "FAILED")
            
            sorter[j].time = end_time - start_time
            uniform_results.append({'Algorithm': names[j], 'Seed': SEED, 'Data Size': SIZE, 'Runtime': sorter[j].time, 'Theoretical Big-O': 0})

### Almost-sorted loop beginning
for SIZE in SIZES:
    
    for SEED in SEEDS: #conduct a trial for every seed and algorithm at the current data size.
        random.seed(SEED)

        swap1, swap2 = genSwapmap(SIZE) #Create consistent swapmap for the seed

        #create random data.
        data = []
        for i in range(SIZE):
            data.append(random.randint(0,1000))
        
        data_save = data.copy()
        test_data = sorted(data)
        data = sorted(data_save) #create sorted dataset

        for i, j in zip(swap1, swap2):
            data[i], data[j] = data[j], data[i]

        for j in range(len(sorter)):
            data = data_save.copy()  # Reset data to its original unsorted state before sorting.
            start_time = time.perf_counter()
            sorter[j].sort(data)
            end_time = time.perf_counter()

            if test_data != data:
                print(names[j], SIZE, SEED,  "FAILED")
            
            sorter[j].time = end_time - start_time
            almost_results.append({'Algorithm': names[j], 'Seed': SEED, 'Data Size': SIZE, 'Runtime': sorter[j].time, 'Theoretical Big-O': 0})


uniform_results_df = pd.DataFrame(uniform_results)
almost_results_df = pd.DataFrame(almost_results)
print(uniform_results_df)
print(almost_results_df)
#uniform_results_df.to_csv('uniform_results.csv', index=False)

# Almost Sorted Testing and Results

#almost_sorted_results_df = pd.DataFrame(almost_sorted_results)
#almost_sorted_results_df.to_csv('almost_sorted_results.csv', index=False)