class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        maxi=0
        i=0
        j=0
        while j<len(s):
            if s[j] not in d:
                d[s[j]]=1
                maxi=max(maxi,(j-i+1))
            else:
                while s[i]!=s[j]:
                    del d[s[i]]
                    i+=1
                d[s[j]]=1
                i+=1
            j+=1
        return maxi
                
                 
            
                