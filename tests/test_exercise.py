import pytest
from simple.second_exercise import hello_world, Calculator


def test_hello_world():
    # configure
    expected = "Hello World"
    # act
    res = hello_world()
    # test
    assert expected == res

ADD_PARAMETERS = [
    (1, 2, 3),
    ("1", '2', "12"),
    (1, -2, -1),
    (1+1j, -1-1j, 0),
]

@pytest.mark.parametrize("val1, val2, expected", ADD_PARAMETERS)
def test_add(val1, val2, expected):
    # init
    a, b, expected = val1, val2, expected
    calc = Calculator()

    # act
    res = calc.add(a, b)

    # test
    assert res == expected


def test_substr():
    # init
    a, b, expected = 3, 2, 1

    # act
    res = Calculator.susbtr(a, b)
    # test
    assert res == expected