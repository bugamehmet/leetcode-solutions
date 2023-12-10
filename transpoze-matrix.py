# 867. Transpose Matrix

class Solution(object):
    def transpose(self, matrix):
        result = []
        for i in range(len(matrix[0])): 
            column = []
            for j in range(len(matrix)):  
                column.append(matrix[j][i])
            result.append(column)
        return result