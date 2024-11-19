import pytest
from safe_calculator import SafeCalculator

class Authorizer:
    def authorize(self):
        return True


def test_divide_should_not_raise_any_error_when_authorized():
    
    # TODO: write a test that fails due to the bug in
    safe_calculator = SafeCalculator(Authorizer())

    actual = safe_calculator.add(1, 2)
    expected = 3
    
    assert actual == expected, f'The result should be {expected} but was {actual}'
        


