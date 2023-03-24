class Solution:
    def reverse_digit(self, n):
        # Code here
        rev = 0
        while n > 0:
            digit = n % 10
            rev = (rev * 10)  + digit
            n //=10
            
        return rev