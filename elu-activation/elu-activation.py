import math
import numpy as np
def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    x= np.array(x)
    results = np.where(x>0, x, alpha * (np.exp(x) - 1))
    return results.tolist()
    