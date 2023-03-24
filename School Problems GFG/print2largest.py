class Solution:

	def print2largest(self,arr, n):
		# code here
		arr = sorted(set(arr))
		if len(arr) < 2:
		    return -1
		    
		else:
		    return arr[-2]