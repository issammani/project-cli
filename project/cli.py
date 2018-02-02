"""
project
 
Usage:
  project init
  project -h | --help
  project --version
 
Options:
  -h --help                         Show this screen.
  --version                         Show version.
 
Examples:
  project init
 
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/issamouu69/project-cli
"""
 
 
from inspect import getmembers, isclass
 
from docopt import docopt
 
from __init__ import __version__ as VERSION


 
def main():
    """Main CLI entrypoint."""
    import commands
    options = docopt(__doc__, version=VERSION)

if __name__ == '__main__':
  main()