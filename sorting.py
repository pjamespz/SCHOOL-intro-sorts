# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.
import random as rand
from collections.abc import Iterable

class MergeSort:
	def __init__(self):
		self.time = 0

	def sort(self, data):
		'''
		Sort the list data using MergeSort
	 	@param list data to be sorted
		'''
		self.sortHelper(data, 0, len(data))
		print(data)

	def sortHelper(self, data, low, high):
		'''
		MergeSort helper method.  Sorts data >= start and < end
		
		@param list data to be sorted
		@param low start of the data to be sorted
		@param high end of the data to be sorted (exclusive)
		'''
		
		if high - low > 1:
			mid = low + (high-low)//2
			# TODO: finish recursive calls to 2 halves
			self.sortHelper(data, low, mid)	
			self.sortHelper(data, mid, high)
			self.merge(data, low, mid, high)

	def merge(self, data, low, mid, high):
		'''
		Merge data >= low and < high into sorted data.  Data >= low and < mid are in sorted order.
		Data >= mid and < high are also in sorted order
		
		@param data the partially sorted data
		@param low bottom index of the data to be merged
		@param mid midpoint of the data to be merged
		@param high end of the data to be merged (exclusive)
		
		Note: the merged data must be in the same data array that
		      was passed as a parameter.
		'''
		temp = []
		i = low
		j = mid

		while (i < mid and j < high):
			if data[i] <= data[j]:
				temp.append(data[i])
				i += 1
			else:
				temp.append(data[j])
				j += 1
		while (i < mid):
			temp.append(data[i])
			i += 1
		while (j < high):
			temp.append(data[j])
			j += 1
		for num in range(len(temp)):
			data[low + num] = temp[num]


class QuickSort:
	def __init__(self):
		self.time = 0

	def swap(self, data, index1, index2):
		temp = data[index1]
		data[index1] = data[index2]
		data[index2] = temp

	def sort(self, data): # O(n log n) expected, O(n^2) worst depending on pivot
		'''
		Sort the list data using QuickSort
	 	@param list data to be sorted
		'''
		self.sortHelper(data, 0, len(data)-1)
		print(data)

	def sortHelper(self, data, low, high):
		'''
 		Helper method for Quicksort.  Sorts data so that data[lo .. j-1] <= data[j] <= data[j+1 .. hi]
	 	
	 	@param data data to be sorted
	 	@param low start of the data to be sorted (inclusive)
	 	@param high end of the data to be sorted (exclusive)
		'''
		if high <= low:
			return
		
		pivot = self.partition(data, low, high)

		# TODO: Finish recursive calls to sortHelpter
		self.sortHelper(data, low, pivot - 1)	
		self.sortHelper(data, pivot + 1, high)

	def partition(self, data, low, high):
		i = low - 1
		pivot = data[high]
		for j in range(low, high):
			if data[j] <= pivot:
				i += 1
				self.swap(data, i, j)
		i += 1
		self.swap(data,i,high)
		return i


class InsertionSort:
	def __init__(self):
		self.time = 0

	def swap(self, data, index1, index2):
		temp = data[index1]
		data[index1] = data[index2]
		data[index2] = temp

	def sort(self, data): # O(n^2), but O(n) possible if pre-sorted
		'''
		Sort the list data using InsertionSort
	 	@param list data to be sorted
		'''
		# TODO - complete implementation
		for i in range(1, len(data)):
			current = data[i]
			j = i
			while (0 < j and current < data[j-1]):
				self.swap(data, j, j - 1)
				j -=1
			data[j] = current
		print(data)


class ShellSort:
	def __init__(self, gap_list):
		self.time = 0
		self.gap_list = gap_list

	def swap(self, data, index1, index2):
		temp = data[index1]
		data[index1] = data[index2]
		data[index2] = temp

	def sort(self, data):
		'''
		Sort the list data using ShellSort
	 	@param list data to be sorted
		Gap sequence is stored in self.gap_list upon construction
		'''
		# TODO - complete implementation
		for gap in self.gap_list:
			for i in range(gap, len(data)):
				current = data[i]
				j = 1
				while (gap <= j and current < data[j - gap]):
					self.swap(data, j, j - gap)
					j -= gap
				data[j] = current
		print(data)


class BucketSort:
	def __init__(self, range):
		self.time = 0
		self.range = range + 1
		self.table = [None]*self.range
		self.max = 0

	def insert(self, elem):
		if self.table[elem] == None:
			self.table[elem] = [elem]
		else:
			self.table[elem].append(elem)

	def sort(self, data):
		'''
		Sort the list data using BucketSort
	 	@param list data to be sorted
		bucket table is self.table
		'''
		# TODO - complete implementation
		pass


class RadixSort:
	def __init__(self):
		self.time = 0
		self.table = [None]*10
		self.max = 0
		self.digits = 0

	def insert(self, elem, iter):
		# TODO - complete implementation
		# Refer to insert for BucketSort
		pass

	def sort(self, data):
		'''
		Sort the list data using RadixSort
	 	@param list data to be sorted
		bucket table is self.table with 10 entries
		'''
		# TODO - complete implementation
		pass




	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
