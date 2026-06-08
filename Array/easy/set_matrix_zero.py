from typing import List
def markRow(self,arr, row):
           for col in range(len(arr[0])):
             if arr[row][col] != 0:
                arr[row][col] = -1

def markCol(self,arr, col):
          for row in range(len(arr)):
            if arr[row][col] != 0:
               arr[row][col] = -1

def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    self.markRow(matrix,i)
                    self.markCol(matrix,j)

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0