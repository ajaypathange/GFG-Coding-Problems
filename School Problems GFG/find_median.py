class Solution:
	def find_median(self, v):
		# Code here
		n = len(v)
		v.sort()
		
		if n%2 == 0:
		    median1 = v[n//2]
		    median2 = v[n//2-1]
		    median = (median1+median2) / 2
	    else:
	        median = v[n//2]
	        
        return int(median)