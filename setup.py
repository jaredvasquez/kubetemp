from setuptools import setup

setup(
    name='kubetemp',
    version='0.1.1',
    author='Jared Vasquez',
    description=(
        'Tool for generating kubernetes (k8s) manifests using Jinja templates.'
    ),
    url='https://github.com/jgv7/kubetemp',
    license='MIT',
    install_requires=[
        'Click>=7.0',
        'jinja2>=2.10',
        'pyyaml',
    ],
    packages=['kubetemp'],
    python_requires=">=3.6",
    scripts=['bin/kubetemp'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    zip_safe=False,
)
