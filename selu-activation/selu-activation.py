import math
import numpy as np

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    x= np.array(x)
    results = np.where(x>0, 1.0507 * x, 1.0507 * 1.6733 * (np.exp(x)-1))
    return results.tolist()