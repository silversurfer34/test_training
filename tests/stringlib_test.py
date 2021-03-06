from simple.stringlib import custom_capitalize, basic_capitalize
import pytest


def test_capitalize():
    # initialize
    value = "test value"
    expected = "Test value"
    # act
    res = custom_capitalize(value)
    # test
    assert res == expected


# TODO Write a test for empty values
def test_none_capitalize():
    # initialize
    value = ""
    expected = ""
    # act
    res = custom_capitalize(value)
    # test
    assert res == expected


# TODO Write a test for string starting with a number
def test_none2_capitalize():
    # initialize
    value = "9 abcd"
    expected = "9 abcd"
    # act
    res = custom_capitalize(value)
    # test
    assert res == expected


# TODO Write a test to find a failure
def test_exception_capitalize():
    # initialize
    value = 253
    with pytest.raises(AttributeError):
        res = basic_capitalize(value)


def test_wrong_type_capitalize():
    # initialize
    value = 253
    expected = 253
    # act
    res = custom_capitalize(value)
    # test
    assert res == expected


# TODO Add parametrized tests examples
