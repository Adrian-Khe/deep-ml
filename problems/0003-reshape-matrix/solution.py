import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    
    lines_a = len(a)
    columns_a = len(a[0])
    ns_lines, ns_columns = new_shape


    if lines_a * columns_a != ns_lines * ns_columns:
        return []
    
    reshaped_matrix = [[0] * ns_columns for _ in range(ns_lines)]
    for i in range(lines_a):
        for j in range(columns_a):
            k = i * columns_a + j  # index dans la liste aplatie
            reshaped_matrix[k // ns_columns][k % ns_columns] = a[i][j]

    return reshaped_matrix

