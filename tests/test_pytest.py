import pytest


@pytest.fixture(scope="session")
def init_value():
    value = 5
    print("init value : ", value)
    return value


@pytest.fixture
def echo(init_value):
    print("echo value : ", init_value)
    return init_value


def test_upper(init_value, echo):
    assert "foo".upper() == "FOO"
    init_value += 1
    print("value : ", init_value)


def test_lower(init_value, echo):
    assert "FOO".lower() == "foo"
    init_value += 1
    print("value : ", init_value)


def test_split(init_value, echo):
    assert ["a", "b"] == "a b".split()
    init_value += 1
    print("value : ", init_value)
