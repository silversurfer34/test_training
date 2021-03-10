from simple.stringlib import safe_capitalize, basic_capitalize
import pytest


def test_capitalize():
    # initialize
    value = "test value"
    expected = "Test value"
    # act
    res = basic_capitalize(value)
    # test
    assert res == expected


# TODO Write a test for empty values
def test_empty_capitalize():
    # initialize
    value = ""
    expected = ""
    # act
    res = basic_capitalize(value)
    # test
    assert res == expected


# TODO Write a test for string starting with a number
def test_number_capitalize():
    # initialize
    value = "9 abcd"
    expected = "9 abcd"
    # act
    res = basic_capitalize(value)
    # test
    assert res == expected


# TODO Write a test to find a normal failure
# AttributeError exception is sent when data type is not correct
# To test an exception is sent use
#
# with pytest.raise(ExceptionClass):
#   your code to test
#
def test_exception_capitalize():
    # initialize
    value = 253
    with pytest.raises(AttributeError):
        res = basic_capitalize(value)


# TODO Write a test for none values (value = None)
@pytest.mark.skip
def test_none_capitalize():
    # initialize
    value = None
    expected = None
    # act
    res = basic_capitalize(value)
    # test
    assert res == expected


# TODO Write a new safer version of capitalize which return the input value
# if the type is not string
# To test if an object is an instance of a given class use isinstance(data, class):
# The name of the new function will be safe_capitalize
def test_wrong_type_capitalize():
    # initialize
    value = 253
    expected = 253
    # act
    res = safe_capitalize(value)
    # test
    assert res == expected


# TODO Add parametrized tests
# with the following input values "normal string", "", "123 string"
# see https://docs.pytest.org/en/stable/parametrize.html
TEST_DATA = [("normal string", "Normal string"), ("", ""), ("123 string", "123 string")]


@pytest.mark.parametrize("data,expected", TEST_DATA)
def test_capitalize_values(data, expected):
    # act
    res = basic_capitalize(data)
    # test
    assert res == expected
