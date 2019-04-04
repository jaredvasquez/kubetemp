# kubetemp

[![Build Status](https://travis-ci.org/jgv7/kubetemp.svg?branch=master)](https://travis-ci.org/jgv7/kubetemp)
[![Coverage Status](https://coveralls.io/repos/github/jgv7/kubetemp/badge.svg)](https://coveralls.io/github/jgv7/kubetemp)
[![Updates](https://pyup.io/repos/github/jgv7/kubetemp/shield.svg)](https://pyup.io/repos/github/pyupio/pyup/)
[![PyPI version](https://badge.fury.io/py/kubetemp.svg)](https://badge.fury.io/py/kubetemp)
[![pypi supported versions](https://img.shields.io/pypi/pyversions/kubetemp.svg)](https://pypi.python.org/pypi/kubetemp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Tool for generating kubernetes (k8s) manifests using Jinja templates.

## Installation

Kubetemp requires Python 3.6 or greater and can be installed by pip:

```
pip install kubetemp
```

#### Local installation 

To install the `kubetemp` package locally, simply run:

```
pip install .
```

For development, it is useful to install in editable mode:

```
pip install -e .
```


## Usage

Usage instructions from `kubetemp` CLI tool:

```
Usage: kubetemp [OPTIONS] TEMPLATE

  Renders Jinja template with parameters

Options:
  -f, --file PATH      Read parameters from JSON or YAML file
  -p, --param TEXT...  Define parameters to render template
  -o, --output PATH    Write rendered template to output file
  --help               Show this message and exit.
```

#### Examples

Render template with parameters from `parameters.yaml` and the parameter
`TAG=0.2.7`. If the `TAG` parameter is defined in the parameters file it 
will be over-written by the value provided in the CLI argument.

```
kubetemp template-file.yaml -f parameters.yaml -p TAG 0.2.7
```

Render template with parameters `IMAGE=docker/myimage` and `TAG=0.2.7`. 

```
kubetemp template-file.yaml -p IMAGE docker/myimage -p TAG 0.2.7
```

Render template with parameters from `parameters.yaml` and output the
results to `output-rendered.yaml`. If an output file is not specified, then
results will be output to STDOUT.

```
kubetemp template-file.yaml -p parameters.yaml -o output-rendered.yaml
```

Templates can also be provided via STDIN by using "-" inplace of a template
filepath

```
cat template-file.yaml | kubetemp - -p IMAGE docker/myimage -p TAG 0.2.7
```
