import numpy as np

import src.matrix

def test_foo():
    result = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ])

    assert (src.matrix.foo() == result).all()