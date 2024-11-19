
from discount_applier import DiscountApplier
from user import User
import pytest

class UserTest(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.notified = 0

class Notifier:
    def notify(self, user : UserTest, message):
        user.notified += 1

@pytest.fixture
def discount_applier():
    return DiscountApplier(Notifier())
    
@pytest.fixture
def users():
    return [UserTest('Alice', 'al.ice@gmail.com'), UserTest('Bob', 'bo.b@gmail.com'), UserTest('Charlie', 'Char.lie@mail.fr')]
        
def test_apply_v1(users, discount_applier):
    
    temp_users = users.copy()
    
    # TODO: write a test that fails due to the bug in
    discount_applier.apply_v1(50, temp_users)
    
    # Check that all users have been notified, if not, the test fails
    for i in range(len(temp_users)):
        assert temp_users[i].notified == 1, f'The user at position {i} should have been notified once but was notified {temp_users[i].notified} times'


def test_apply_v2(users, discount_applier):
    
    temp_users = users.copy()

    # TODO: write a test that fails due to the bug in 
    discount_applier.apply_v2(50, temp_users)

    # Check that all users have been notified, if not, the test fails
    for i in range(len(temp_users)):
        print(temp_users[i].notified)
        assert temp_users[i].notified == 1, f'The user at position {i} should have been notified once but was notified {temp_users[i].notified} times'

