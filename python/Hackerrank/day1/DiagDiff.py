def diagonalDifference(arr):
    n = len(arr)
    d1 = sum(arr[i][i] for i in range(n))
    d2 = sum(arr[i][n-i-1] for i in range(n))
    return abs(d1 - d2)

print(diagonalDifference([[1,2,3],[4,5,6],[7,8,9]]))
