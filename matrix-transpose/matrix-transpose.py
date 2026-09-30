import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    rows=len(A)
    cols=len(A[0])

    transposed_array=np.zeros((cols, rows))

    for i in range(rows):
        for j in range(cols):
            transposed_array[j][i]=A[i][j]

    return transposed_array
            
    
    pass
