"""Demonstrate -lf and -ff with failing tests."""

import pytest
from pytest import approx


testdata = [
    # x, y, expected
    (1.01, 2.01, 3.02),
    (1e25, 1e23, 1.1e25),
    (1.23, 3.21, 4.44),
    (0.1, 0.2, 0.3),
    (1e25, 1e24, 1.1e25)
]


@pytest.mark.parametrize("x,y,expected", testdata)
def test_a(x, y, expected):
    """Demo approx()."""
    sum_ = x + y
    assert sum_ == approx(expected)

#Andy version using fixture parametrize - hal - 02/22/19
def id_func(fx_value):
#	x, y, z = fx_value
	return '{}, {}, {}'.format(*fx_value)

@pytest.fixture(params=testdata, ids=id_func)
def sum_fixture_parm(request):
	return request.param

def test_fixture_parma(sum_fixture_parm):
    x, y, expected = sum_fixture_parm
#    print(sum_fixture_parm)
    sum_ = x + y
    assert sum_ == approx(expected)


