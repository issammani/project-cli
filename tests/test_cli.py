"""Tests for main cli """


from subprocess import PIPE, Popen as popen
from unittest import TestCase, main
import re
from project import __version__

class TestHelp(TestCase):
    def test_help(self):
        output = popen(['project', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in str(output) )
 
        output = popen(['project', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in str(output) )


class TestVersion(TestCase):
    def test_version(self):
        output = popen(['project', '--version'], stdout=PIPE).communicate()[0]
        match = re.search('(\d.\d.\d)', str(output.strip()) )
        self.assertEqual(match.group(0), __version__)

if __name__ == '__main__':
    main()