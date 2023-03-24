class Solution:
    def isDigitSumPalindrome(self,N):
        #code here
        sum = 0
        while (N !=0):
            sum =sum+(N%10)
            N=N//10
        
        
        sum_str = str(sum) 
        if sum_str == sum_str[::-1]:
            e = int("1")
            return e
            
        else:
            e = int("0")
            return e