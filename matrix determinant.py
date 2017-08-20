import math

def determinant(matrix):
    dimention = len(matrix[0])
    if dimention == 1:
        return matrix[0][0]
    else:
        result = 0
        for i in range(dimention):
            result += math.pow(-1, i) * matrix[0][i] * determinant([[row[a] for a in range(dimention) if a != i] for row in matrix[1:]])
        return int(result)

if __name__ == '__main__':
    print(determinant([[1,2],[3,4]]))