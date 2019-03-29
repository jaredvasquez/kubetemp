import click
from click.testing import CliRunner
import pytest

from kubetemp.cli import _render_template


@pytest.fixture
def runner():
    return CliRunner()


@pytest.mark.parametrize('name', ['Joe', 'John', 'Jim', 123, ''])
def test_render_template(runner, name):
    result = runner.invoke(
        _render_template,
        ['tests/files/test.tmpl', '-p', 'name', name]
    )
    assert result.exit_code == 0
    assert result.output == f'Hello, {name}!\n'
