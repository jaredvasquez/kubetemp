import pytest

from kubetemp import update_params


def test_update_params():
    original = {'old': True}
    new_params = {'new': True, 'old': False}
    update_params(original, new_params)
    assert 'new' in original
    assert original['new'] is True
    assert original['old'] is False
