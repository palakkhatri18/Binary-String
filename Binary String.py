class Solution:
    
    #Function to count the number of substrings that start and end with 1.
    def binarySubstring(self,n,s):
        #code here
        count = s.count('1')
        ans=((count)*(count-1))/2
        return int(ans)