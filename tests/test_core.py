import pytest

from jinja2 import Template
from kubetemp.core import (
    _check_valid_path,
    _load_template,
    _render_template,
)


def test_check_valid_path():
    # Raise exception when path does not exist
    with pytest.raises(ValueError, match='does not exist.$'):
        _check_valid_path('path/does/not/exist')

    # Raise exception when path is not a file
    with pytest.raises(TypeError, match='is not a file.$'):
        _check_valid_path('tests/files')

    # Do nothing when path is fine
    _check_valid_path('tests/files/test1.tmpl')


def test_load_template():
    # Raise exception when path does not exist
    with pytest.raises(ValueError, match='does not exist.$'):
        _load_template('path/does/not/exist')

    # Raise exception when path is not a file
    with pytest.raises(TypeError, match='is not a file.$'):
        _load_template('tests/files')

    # Test successfully loading a template
    temp = _load_template('tests/files/test1.tmpl')
    assert isinstance(temp, Template)



@pytest.fixture
def test_template():
    return _load_template('tests/files/test1.tmpl')

@pytest.mark.parametrize('name', ['Joe', 'John', 'Jim', 123, '', None])
def test_render_template(test_template, name):
    expected = 'Hello, {name}!'.format(**locals())
    result = _render_template(test_template, **locals())
    assert result == expected
