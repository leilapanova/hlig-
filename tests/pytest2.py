from proj import check_even

def test_check_even():
        assert check_even(4) == True
        assert check_even(7) == False
        assert check_even(0) == True
        assert check_even(-2) == True
        assert check_even(-7) == False