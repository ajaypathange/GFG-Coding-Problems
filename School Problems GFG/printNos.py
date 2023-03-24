class Solution:    
    #Complete this function
    def printNos(self,N):
        if N > 0:
            Solution.printNos(self,N - 1)
            print(N,end=' ')