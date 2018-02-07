"""Tests for main cli """


from subprocess import check_output
from unittest import TestCase, main
import re
from project import __version__

class TestHelp(TestCase):
    def test_help(self):
        output = check_output(['project','-h'])
        self.assertTrue('Usage:' in str(output) )
 
        output = check_output(['project','--help'])
        self.assertTrue('Usage:' in str(output) )


class TestVersion(TestCase):
    def test_version(self):
        output = check_output(['project', '--version'])
        match = re.search('(\d.\d.\d)', str(output.strip()) )
        self.assertEqual(match.group(0), __version__)

        output = check_output(['project', '-v'])
        match = re.search('(\d.\d.\d)', str(output.strip()) )
        self.assertEqual(match.group(0), __version__)

if __name__ == '__main__':
    main()