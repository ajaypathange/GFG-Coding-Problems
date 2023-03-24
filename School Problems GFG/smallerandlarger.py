class Solution:

	def getMoreAndLess(self,arr, n, x):
		# code here
		less = 0
		more = 0
		for i in range(n):
		    if arr[i] <= x and arr[i] >= x:
		        less = less + 1
		        more = more + 1
		        
	        elif arr[i] >= x:
	            more = more + 1
            
            elif arr[i] <= x:
	            less = less + 1
	
	    return less,more