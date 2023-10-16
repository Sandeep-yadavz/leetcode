class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a=[[1]]
        for i in range(rowIndex):
            x=[1]
            for j in range(len(a[-1])-1):
                x.append(a[-1][j]+a[-1][j+1])
            x.append(1)
            a.append(x)
        return a[rowIndex]
        