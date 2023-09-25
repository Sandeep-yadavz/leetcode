class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat=[[0 for i in range(n)]for i in range(n)]
        h_u=0
        h_b=n
        v_l=0
        v_r=n
        c=1
        fill=1
        while h_u<h_b or v_l<v_r:
            for i in range(v_l,v_r):
                mat[h_u][i]=fill
                fill+=1
                c+=1
            h_u+=1
            for j in range(h_u,h_b):
                mat[j][v_r-1]=fill
                fill+=1
                c+=1
            v_r-=1
            for k in range(v_r-1,v_l-1,-1):
                mat[h_b-1][k]=fill
                fill+=1
                c+=1
            h_b-=1
            for m in range(h_b-1,h_u-1,-1):
                mat[m][v_l]=fill
                fill+=1
                c+=1
            v_l+=1
        return mat
                


        