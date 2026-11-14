def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    
    res = [[0] * len(b[0]) for _ in range(len(a))] 
    if len(b) != len(a[0]):
        return -1 
    for i in range(len(a)):
        for j in range(len(b[0])):
            summ = 0
            for k in range(len(b)):
                summ += a[i][k] * b[k][j]
            
            res[i][j] = summ
    
    return res