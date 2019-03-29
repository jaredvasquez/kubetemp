import json
import os

from jinja2 import Template
import yaml


def _load_template(template_str):
    """ Loads jinja template object from string """
    return Template(template_str)


def _render_template(template, **params):
    """ Render a jinja template object """
    return template.render(**params)


def render_string(template_str, **params):
    """ Renders output from a jinja template string """
    template = _load_template(template_str)
    return _render_template(template, **params)


def _check_valid_path(path):
    """ Ensure that path exists and is a file """
    if not os.path.exists(path):
        raise ValueError(f'Path "{path}" does not exist.')
    if not os.path.isfile(path):
        raise TypeError(f'Path "{path}" is not a file.')


def _read_json(path):
    """ Read JSON file from path """
    _check_valid_path(path)
    with open(path) as _file:
        return json.load(_file)


def _read_yaml(path):
    """ Read YAML file from path """
    _check_valid_path(path)
    with open(path) as _file:
        return yaml.safe_load(_file)


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
