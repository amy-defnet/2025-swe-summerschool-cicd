from pytest import approx
import numpy as np
from cicdexample.square_plus_one import square_plus_one


def test_square_plus_one():
    """Basic tests for function square_plus_one."""
    assert square_plus_one(0) == 1
    assert square_plus_one(1) == 2
    assert square_plus_one(2) == 5

    l = np.arange(100)
    l2p1 = square_plus_one(l)
    assert all(c == (i ** 2) + 1 for i, c in enumerate(l2p1))

    l = np.arange(10, step=0.2)
    l2p1 = square_plus_one(l)
    assert all(c == approx(((i * 0.2) ** 2) + 1) for i, c in enumerate(l2p1))
