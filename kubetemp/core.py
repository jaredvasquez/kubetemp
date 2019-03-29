import json
import os

from jinja2 import Template
import yaml


def _check_valid_path(path):
    if not os.path.exists(path):
        raise ValueError(f'Path "{path}" does not exist.')
    if not os.path.isfile(path):
        raise ValueError(f'Path "{path}" is not a file.')


def _load_template(path):
    """ Loads template object from filepath """
    _check_valid_path(path)
    with open(path) as _file:
        return Template(_file.read())


def _render_template(template, **params):
    return template.render(**params)


def render_path(path, **params):
    template = _load_template(path)
    return _render_template(template, **params)


def _read_json(path):
    """ Read JSON file from path """
    if path is None:
        return {}

    _check_valid_path(path)
    with open(path) as _file:
        return json.load(_file)


def _read_yaml(path):
    """ Read YAML file from path """
    if path is None:
        return {}

    _check_valid_path(path)
    with open(path) as _file:
        return yaml.load(_file)


def read_params(path):
    if path is None:
        return {}
    elif path.endswith('.json'):
        return _read_json(path)
    elif path.endswith(('.yml', '.yaml')):
        return _read_yaml(path)
    else:
        raise ValueError(f'Path "{path}" does not have JSON or YAML extension')


def update_params(params_dict, json_dict):
    if json_dict is None:
        return
    params_dict.update(json_dict)


def write_output(output, path):
    with open(path, 'w') as _file:
        _file.write(output)
