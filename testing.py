#import ref_sorting 
import random
import time

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
			print(f"Indices: {low}, {mid}, {high}")
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
		
	
testData = [15,8,20,50,4,7,5,9]
testObj = MergeSort()
testObj.sort(testData)