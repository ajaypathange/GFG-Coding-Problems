class Solution:
    def getTable(self,N):
        # code here
        
        table = []
        for i in range(1,11):
            S = N * i
            table.append(S)
            
        return table