from setuptools import setup

setup(
    name='kubetemp',
    version='0.0.1',
    description='Tool for generating kubernetes manifests using JINJA templates.',
    url='https://github.com/jgv7/kubetemp',
    author='Jared Vasquez',
    license='MIT',
    packages=['kubetemp'],
    scripts=['bin/kubetemp'],
    install_requires=[
        'Click>=7.0',
        'jinja2>=2.10',
        'pyyaml'
    ],
    zip_safe=False,
)
