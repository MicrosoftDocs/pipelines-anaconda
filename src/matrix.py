import numpy as np

def foo():
    a = np.array([
        [1, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ])

    return a * np.identity(3)