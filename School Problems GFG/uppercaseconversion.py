class Solution:
    def transform(self, s):
        # code here
        words = s.split()
        capital =[]
        for i in words:
            capital.append(i.capitalize())
        
        out = " ".join(capital)
        return out