import json
import os

from jinja2 import Template
import yaml


def _check_valid_path(path):
    """ Ensure that path exists and is a file """
    if not os.path.exists(path):
        raise ValueError(f'Path "{path}" does not exist.')
    if not os.path.isfile(path):
        raise TypeError(f'Path "{path}" is not a file.')


def _load_template(path):
    """ Loads jinja template object from filepath """
    _check_valid_path(path)
    with open(path) as _file:
        return Template(_file.read())


def _render_template(template, **params):
    """ Render a jinja template object """
    return template.render(**params)


def render_path(path, **params):
    """ Renders a jinja template from filepath """
    template = _load_template(path)
    return _render_template(template, **params)


def _read_json(path):
    """ Read JSON file from path """
    _check_valid_path(path)
    with open(path) as _file:
        return json.load(_file)


def _read_yaml(path):
    """ Read YAML file from path """
    _check_valid_path(path)
    with open(path) as _file:
        return yaml.load(_file, Loader=yaml.FullLoader)


def read_params(path):
    """ Read parameters from JSON or YAML file path """
    if path is None:
        return {}
    elif path.endswith('.json'):
        return _read_json(path)
    elif path.endswith(('.yml', '.yaml')):
        return _read_yaml(path)
    else:
        raise ValueError(f'Path "{path}" does not have a known extension.')


def write_output(output, path):
    """ Write output string to file at path """
    with open(path, 'w') as _file:
        _file.write(output)
