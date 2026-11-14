def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    
    res : list[float]
    if mode == 'column':
        res = [0]*len(matrix[0])

        for i in range(len(matrix[0])):
            summ = 0
            for j in range(len(matrix)):
                summ += matrix[j][i]
            res[i] = summ / len(matrix)
        return res

    elif mode == 'row':
        res = [0]*len(matrix)
        for i in range(len(matrix)):
            summ =0
            
            for j in range(len(matrix[0])):
                summ += matrix[i][j]
            res[i]= summ / len(matrix[0])
        return res
    else:
        raise ValueError("mode must be 'row' or 'column'")