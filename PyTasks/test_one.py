def test_passing():
    assert (1, 4, 3) == (1, 2, 3)

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5