class Solution:

	def valueEqualToIndex(self,arr, n):
		# code here
		result = []
		for i in range(len(arr)):
		    if arr[i] == i + 1:
		        result.append(i+1)
		        
	    return result