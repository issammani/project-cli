"""Tests for project init"""


from subprocess import check_output
from unittest import TestCase, main
import os,shutil
from project.commands import init


class TestInit(TestCase):   
    pass # for now

class TestProject(TestCase):
    
    # some mock data
    @classmethod
    def setUpClass(self):
        # make temp dir
        os.makedirs('../../temp')
        # navigate to that dir
        os.chdir('../../temp')
        empty_dict = {  
            'owner_name'  : '',
            'owner_email' : '',
            'entry_point' : '',
            'description' : '',
            'license' : '',
            'readme'  : '',
        }
        self.p = init.Project(empty_dict)
    
    @classmethod
    def tearDownClass(self):
        os.chdir('..')
        #remove created directory
        shutil.rmtree('temp')

    def test_empty_project(self):
        # make project
        self.p.make()
        #check file existance
        self.assertTrue('main.py' in os.listdir('.'))

if __name__ == '__main__':
    main()