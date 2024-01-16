import pytest
from lesson_8_9_dz import add_numbers


# 1
def test_add_1():
    assert add_numbers(1, 2, 3) == 6


def test_add_2():
    assert add_numbers(3, 5, 7) == 15


def test_add_3():
    assert add_numbers(10, 15, 11) == 36


# 2
@pytest.mark.parametrize("var_1, var_2, var_3, result", [
    pytest.param(3, 5, 7, 15, id="simple"),
    pytest.param(-5, 6, 2, 3, id="with negative"),
    pytest.param(-2, -6, 3, -5, id="one positive")])
def test_add_set(var_1, var_2, var_3, result):
    assert add_numbers(var_1, var_2, var_3) == result


# 3
list_add_test = [(3, 5, 7, 15), (-5, 6, 2, 3), (-2, -6, 3, -5)]


@pytest.mark.parametrize("var_1, var_2, var_3, result", list_add_test)
def test_add_set_2(var_1, var_2, var_3, result):
    assert add_numbers(var_1, var_2, var_3) == result
