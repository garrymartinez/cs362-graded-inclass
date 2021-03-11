import calculator


def test_add():
    assert 20 == calculator.add(13, 7)


def test_subtract():
    assert 12 == calculator.subtract(20, 8)
