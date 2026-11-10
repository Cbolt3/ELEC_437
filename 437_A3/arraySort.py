from bubble_sort import bubbleSort
from quick_sort import quick_sort
import numpy as np

def populateArray():
    rng = np.random.default_rng()
    array = rng.integers(low=1, high=99999, size=100000)
    return array

