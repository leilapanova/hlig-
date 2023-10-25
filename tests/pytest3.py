from proj import count_digits

def test_count_digits():
    assert count_digits(0) == 1
    assert count_digits(12345) == 5
    assert count_digits(9876543210) == 10
    assert count_digits(-123) == 4