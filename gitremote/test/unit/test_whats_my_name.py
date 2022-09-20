import pytest

from gitremote.whats_my_name import my_name_is

#To verify my email
def test_my_name_is():
    assert "vjjimenezdiaz@my.waketech.edu" == my_name_is()
