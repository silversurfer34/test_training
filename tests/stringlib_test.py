from simple.stringlib import basic_capitalize
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
    pass


# TODO Write a test for string starting with a number
def test_number_capitalize():
    pass


# TODO Write a test to find a normal failure
# AttributeError exception is sent when data type is not correct
# To test an exception is sent use
#
# with pytest.raise(ExceptionClass):
#   your code to test
#
def test_exception_capitalize():
    pass


# TODO Write a test for none values (value = None)
def test_none_capitalize():
    pass


# TODO Write a new safer version of capitalize which return the input value
# if the type is not string
# To test if an object is an instance of a given class use isinstance(data, class):
# The name of the new function will be safe_capitalize
def test_wrong_type_capitalize():
    pass


# TODO Add parametrized tests
# with the following input values "normal string", "", "123 string"
# see https://docs.pytest.org/en/stable/parametrize.html
def test_capitalize_values():
    pass
