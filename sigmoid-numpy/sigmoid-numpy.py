import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    if isinstance(x, list):
        array = np.array(x)
        # exponents = np.exp(-array)
        # results = np.array([])
        results = 1 / (1 + np.exp(-array))
        
        # for ex in exponents:
        #     results = np.append(results, (1/(1 + ex )))
        return results
    else:
        return 1 / (1 + np.exp(-x))
            
    pass