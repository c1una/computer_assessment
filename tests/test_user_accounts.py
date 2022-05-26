import pytest
from user_accounts.user_accounts import get_user_accounts, output

def test_output():
    assert get_user_accounts("Darwin") > 0
