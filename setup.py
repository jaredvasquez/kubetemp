from setuptools import setup

setup(
    name='kubetemp',
    version='0.2.3',
    author='Jared Vasquez',
    url='https://github.com/jgv7/kubetemp',
    long_description='https://github.com/jgv7/kubetemp',
    description=(
        'Tool for generating kubernetes (k8s) manifests using Jinja templates.'
    ),
    license='MIT',
    install_requires=[
        'Click>=7.0',
        'jinja2>=2.10',
        'PyYAML<=3.13,>=3.10',
    ],
    packages=['kubetemp'],
    python_requires=">=3.6",
    entry_points='''
        [console_scripts]
        kubetemp=kubetemp.cli:cli
    ''',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    zip_safe=False,
)
