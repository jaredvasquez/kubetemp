import uuid

import pytest

from jinja2 import Template
from kubetemp.core import (
    _check_valid_path,
    _load_template,
    _read_json,
    _read_yaml,
    _render_template,
    read_params,
    render_string,
    write_output,
)


TEMPLATE_STR = "Hello, {{name}}!"


def test_check_valid_path():
    # Raise exception when path does not exist
    with pytest.raises(ValueError, match="does not exist.$"):
        _check_valid_path("path/does/not/exist")

    # Raise exception when path is not a file
    with pytest.raises(TypeError, match="is not a file.$"):
        _check_valid_path("tests/files")

    # Do nothing when path is fine
    _check_valid_path("tests/test_core.py")


def test_load_template():
    # Test successfully loading a template
    temp = _load_template(TEMPLATE_STR)
    assert isinstance(temp, Template)


@pytest.fixture
def test_template():
    return _load_template(TEMPLATE_STR)


@pytest.mark.parametrize("name", ["Joe", "John", "Jim", 123, "", None])
def test_render_template(test_template, name):
    expected = f"Hello, {name}!"
    result = _render_template(test_template, **locals())
    assert result == expected


@pytest.mark.parametrize("name", ["Joe", "John", "Jim", 123, "", None])
def test_render_string(name):
    expected = f"Hello, {name}!"
    result = render_string(TEMPLATE_STR, **locals())
    assert result == expected


def test_read_json():
    params = _read_json("tests/files/params.json")
    assert len(params) == 2
    assert set(params.keys()) == {"age", "name"}
    assert params["age"] == 30
    assert params["name"] == "Tester"


@pytest.mark.parametrize("ext", ["yml", "yaml"])
def test_read_yaml(ext):
    filepath = f"tests/files/params.{ext}"
    params = _read_yaml(filepath)
    assert len(params) == 2
    assert set(params.keys()) == {"age", "name"}
    assert params["age"] == 30
    assert params["name"] == "Tester"


@pytest.mark.parametrize("ext", ["json", "yml", "yaml"])
def test_read_params(ext):
    # Raise exception when extension is unknown
    with pytest.raises(ValueError, match="known extension.$"):
        read_params("unknown/file.ext")

    # When path is None return empty dict
    assert read_params(None) == {}

    # Read from params from paths with supported extensions
    filepath = f"tests/files/params.{ext}"
    params = read_params(filepath)
    assert len(params) == 2
    assert set(params.keys()) == {"age", "name"}
    assert params["age"] == 30
    assert params["name"] == "Tester"


def test_write_output(tmpdir):
    # Write a unique hash to the output file
    path = tmpdir.join("test-file.txt")
    output_str = str(uuid.uuid4())
    write_output(output_str, str(path))

    # Output file should match the unique hash we wrote
    assert path.read() == output_str
