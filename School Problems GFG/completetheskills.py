class Solution:
    def scores(self, a, b, cc):
        # Update list cc of length 2 with cc[0] = ca and cc[1] = cb
        # Your code goes here
        a_count = 0
        b_count = 0
        for i in range(3):
            if a[i] > b[i]:
                a_count+=1
            
            elif a[i] < b[i]:
                b_count+=1
        
        cc[0] +=a_count
        cc[1] +=b_count
        return cc
        