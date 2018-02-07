from setuptools import  Command,setup, find_packages
from os.path import abspath, dirname, join


from project import __version__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with  open(join(this_dir, 'LICENSE'), encoding='utf-8') as f:
    license = f.read()


class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from subprocess import check_output, CalledProcessError
        import sys
        """Run all tests!"""
        try:
            check_output('pytest')
        except CalledProcessError as e:
            print(e.output)


setup(
    name = 'project',
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
    extras_require = {
        'test': ['pytest'],
    },
    entry_points = {
        'console_scripts': [
            'project=project.cli:main',
        ],
    },
    cmdclass = {'test': PyTest},
)
