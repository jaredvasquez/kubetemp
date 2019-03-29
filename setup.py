from setuptools import setup

from kubetemp.version import AUTHOR, DESCRIPTION, PROJECT_NAME, URL, VERSION

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    url=URL,
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
