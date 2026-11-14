import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    
    x = [0]*len(A[0])

    for iterations in range(n):
        new_x = [0]*len(A[0])
        for i in range(len(A[0])):
            summ = sum(A[i][j] * x[j] for j in range(len(A)) if i != j ) 
            new_x[i] = (b[i] - summ)/A[i][i]
        x = new_x
    return x