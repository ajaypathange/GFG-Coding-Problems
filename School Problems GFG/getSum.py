class Solution:
    def getSum(self, arr, n):
        # Your code goes here
        sum = 0
        for i in range(n):
            sum = sum + arr[i]
        return sum
    