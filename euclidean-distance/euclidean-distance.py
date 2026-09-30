import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    sum=0
    for i in range(len(x)):
        sum+= (x[i] - y[i])**2

    distance= np.sqrt(sum)
    return distance
        
    pass