import math
import numpy as np
from scipy.special import erf
def gelu(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    errors=np.array([])
    x=np.array(x)
    
    errors=erf(x / math.sqrt(2))
    return x/2 * (1+ errors)

    