class Solution:
    def printTillN(self, N):
    	#code here 
    	if N > 0:
    	    self.printTillN(N-1)
    	    print(N,end=' ')