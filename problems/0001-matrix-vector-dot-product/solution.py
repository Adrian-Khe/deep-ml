def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    nb_lines_a = len(a)
    nb_columns_a = len(a[0])
    nb_lines_b = len(b)

    if  nb_columns_a != nb_lines_b:
        return -1

    res : list[int|float] = [0]*nb_lines_a
    summ : int | float = 0
    for i in range(nb_lines_a):
        summ = 0
        for j in range(nb_columns_a):
            summ += a[i][j] * b[j]
        res[i] = summ 
    
    return res
