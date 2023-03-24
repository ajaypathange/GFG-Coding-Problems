class Solution:
	def is_palindrome(self, n):
	    
	    num_str = str(n)
	    
	    if num_str == num_str[::-1]:
	        e = str("Yes")
	        return e
	        
        else:
            e = str("No")
            return e