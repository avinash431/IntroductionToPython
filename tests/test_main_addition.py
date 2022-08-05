from main import addition, subtraction


def test_addition_use_case1():
    res1 = addition(2, 3)
    assert res1 == 5


def test_addition_use_case2():
    res1 = addition(2, -3)
    assert res1 != 5


def test_addition_use_case3():
    res1 = addition(-2, -3)
    assert res1 == -5


def test_subtraction_use_case_1():
    res1 = subtraction(2, 3)
    assert res1 == -1