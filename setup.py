from setuptools import setup, find_packages
from os.path import abspath, dirname, join


__version__ = __import__('project').__version__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with  open(join(this_dir, 'LICENSE'), encoding='utf-8') as f:
    license = f.read()

setup(
    name = 'py-project',
    version = __version__,
    description = 'Generate a basic python project structure',
    long_description = long_description,
    url = 'https://github.com/issamouu69/py-project-cli',
    author = 'Issam Mani',
    author_email = 'issamouu69@gmail.com',
    license = license,
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt'],
    entry_points = {
        'console_scripts': [
            'project=project.cli:main',
        ],
    },
)
