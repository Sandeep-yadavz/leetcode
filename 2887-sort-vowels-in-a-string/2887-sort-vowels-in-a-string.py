class Solution:
    def sortVowels(self, s: str) -> str:
        temp="AEIOUaeiou"
        c=[]
        l=[]
        for i in s:
            if i in temp:
                if 'A'<=i<='U':
                    c.append(i)
                else:
                    l.append(i)
        c.sort()
        l.sort()
        a=c+l
        cnt=0
        res=""
        for i in s:
            if i in temp:
                res+=a[cnt]
                cnt+=1
            else:
                res+=i
        return res

        