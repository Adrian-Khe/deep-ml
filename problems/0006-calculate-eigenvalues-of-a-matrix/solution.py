import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    trace_m = a+d
    det_m = a*d - b*c

    #We resolve the second degree equation
    delta = trace_m**2 - 4*det_m

    res : list[float] = []
    
    if delta > 0:
        sqrt_delta = math.sqrt(delta)
        res.append((trace_m+ sqrt_delta)/2)
        res.append((trace_m -sqrt_delta)/2)
    elif delta == 0:
        res.append(trace_m/2)
        res.append(trace_m/2)
    else:
        raise ValueError("No Eingen Values for this matrix")
    return res

