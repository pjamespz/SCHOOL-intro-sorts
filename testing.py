from sorting import MergeSort, QuickSort, InsertionSort, ShellSort

merge_sorter = MergeSort()
quick_sorter = QuickSort()
insertion_sort = InsertionSort()
shell_sort = ShellSort([3, 2])
data = [99,1,4,2,7,71,69,1,9,5,10,4,3,1]


merge_sorter.sort(data)
quick_sorter.sort(data)
insertion_sort.sort(data)
#shell_sort.sort(data)