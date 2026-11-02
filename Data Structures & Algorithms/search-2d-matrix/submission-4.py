class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=(len(matrix))
        n=(len(matrix[0]))
        l=0
        r=m*n
        if r==1 and matrix[0][0]==target:
            return True
        elif r==1:
            return False
        k=0
        while l<=r:
            print(l,r)
            k=l+((r-l)//2)
            i=k//n
            j=k%n
            print(k,i,j)
            
            if k>=m*n:
                return False

            if matrix[i][j]==target:
                return True
            if target>matrix[i][j]:
                l=k+1
            if target<matrix[i][j]:
                r=k-1
        return False
        