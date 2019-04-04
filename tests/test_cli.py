import uuid

from click.testing import CliRunner
import pytest

from kubetemp.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


@pytest.mark.parametrize('name', ['Joe', 'John', 'Jim', 123, ''])
def test_param_arguments(runner, name):
    result = runner.invoke(
        cli,
        ['tests/files/test.tmpl', '-p', 'name', name]
    )
    assert result.exit_code == 0
    assert result.output == f'Hello, {name}!\n'


@pytest.mark.parametrize('ext', ['json', 'yaml', 'yml'])
def test_params_from_file(runner, ext):
    result = runner.invoke(
        cli,
        ['tests/files/test.tmpl', '-f', f'tests/files/params.{ext}']
    )
    assert result.exit_code == 0
    assert result.output == f'Hello, Tester!\n'


@pytest.mark.parametrize('ext', ['json', 'yaml', 'yml'])
def test_override_cli_params(runner, ext):
    result = runner.invoke(
        cli,
        [
            'tests/files/test.tmpl',
            '-f', f'tests/files/params.{ext}',
            '-p', 'name', 'Joe',
        ]
    )
    assert result.exit_code == 0
    assert result.output == f'Hello, Joe!\n'


@pytest.mark.parametrize('name', ['Joe', 'John', 'Jim', 123, ''])
def test_stdin_template(runner, name):
    result = runner.invoke(
        cli,
        ['-', '-p', 'name', name],
        input=f'How are you, {name}?'
    )
    assert result.exit_code == 0
    assert result.output == f'How are you, {name}?\n'


def test_write_output(runner, tmpdir):
    path = tmpdir.join('test.txt')
    hash_str = str(uuid.uuid4())
    result = runner.invoke(
        cli,
        [
            'tests/files/test.tmpl',
            '-p', 'name', hash_str,
            '-o', str(path)
        ]
    )
    assert result.exit_code == 0
    assert result.output == ''
    assert path.read() == f'Hello, {hash_str}!'
