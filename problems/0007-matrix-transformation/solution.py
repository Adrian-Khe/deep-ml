import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    det_s = np.linalg.det(S)
    det_t = np.linalg.det(T)

    if abs(det_s) < 1e-10 or abs(det_t) < 1e-10:
        return -1

    else: 
        return np.linalg.inv(np.array(T)) @ np.array(A) @ np.array(S)

