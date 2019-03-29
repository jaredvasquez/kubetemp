import pytest

from kubetemp.core import _check_valid_path


def test_check_valid_path():
    # Raise exception when path does not exist
    with pytest.raises(ValueError, match='does not exist.$'):
        _check_valid_path('path/does/not/exist')

    # Raise exception when path is not a file
    with pytest.raises(TypeError, match='is not a file.$'):
        _check_valid_path('tests/files')

    # Do nothing when path is fine
    _check_valid_path('tests/files/test1.tmpl')
