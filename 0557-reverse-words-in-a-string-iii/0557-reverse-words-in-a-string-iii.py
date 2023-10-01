class Solution:
    def reverseWords(self, s: str) -> str:
        s+=" "
        def helper(st):
            return st[::-1]
        ans=""
        temp=""
        for i in s:
            if i==" ":
                ans+=helper(temp)+" "
                temp=""
            else:
                temp+=i
        return ans[:-1]

        