class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        x=[]
        y=[]
        n = len(mat)
        if n%2==0:
            for i in range(n):
                for j in range(n):
                    if (i ==j) or (i+j == n-1):
                        x.append(mat[i][j])
        else:
            for i in range(n):
                for j in range(n):
                    if (i==j) or (i+j == n-1):
                        if (i==j) and (i+j == n-1):
                            y.append(mat[i][j])
                        else:
                            x.append(mat[i][j])
        return sum(x) + (sum(y))

                    



        