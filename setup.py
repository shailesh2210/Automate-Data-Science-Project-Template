#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Shailesh Gaddam",
    author_email='shaileshgaddam10@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This is a project Template",
    entry_points={
        'console_scripts': [
            'ml_project=ml_project.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ml_project',
    name='ml_project',
    packages=find_packages(include=['ml_project', 'ml_project.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/shailesh2210/ml_project',
    version='0.0.1',
    zip_safe=False,
)
