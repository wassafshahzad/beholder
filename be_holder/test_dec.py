from watcher import watcher
import pytest


class User:
    pass


@watcher
def function_without_types(a, b) -> str:
    return 'pass'


@watcher
def function_with_types(a: str, b: list):
    return 'pass'


@watcher
def function_with_userdef_types(a: str, b: User):
    return "pass"


"""
Test cases for function without types
"""


def test_function_without_types_success():
    assert function_without_types("a", 1) == "pass"


def test_function_without_types_fail():
    with pytest.raises(TypeError):
        function_without_types()


"""
Test cases for functions with types
"""


def test_function_with_types_success():
    assert function_with_types("a", []) == "pass"


def test_function_with_types_fail_TypeError_first_arg():
    with pytest.raises(TypeError):
        function_with_types(1, [])


def test_function_with_types_fail_TypeError_second_arg():
    with pytest.raises(TypeError):
        function_with_types("a", "a")


def test_function_with_types_fail_TypeError_both_arg():
    with pytest.raises(TypeError):
        function_with_types(1, 1)


def test_function_with_types_fail_TypeError_extra_arg():
    with pytest.raises(TypeError):
        function_with_types("1", [], "0")


def test_function_with_types_fail_TypeError_no_arg():
    with pytest.raises(TypeError):
        function_with_types()


"""
Test for User defined Data Types
"""


def test_function_with_userdef_types_success():
    assert function_with_userdef_types("a", User()) == "pass"


def test_function_with_userdef_types_fail():
    with pytest.raises(TypeError):
        function_with_userdef_types("a", 1) == "pass"
