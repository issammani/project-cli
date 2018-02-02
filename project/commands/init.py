"""The init command."""


from json import dumps
from os import path,getcwd
from .config import LICENSES, README
from .base import Base
import time
from string import Template




class Init(Base):
    """Initialize the project"""

    def get_user_infos(self):
        #for now this is the data needed
        dict = {}    
        dict['owner_name']= input("Please enter your name: ")
        dict['owner_email']= input("Please enter your email: ")
        dict['entry_point']= input("Entrypoint file (main.py): ")
        dict['description'] = input("Project description :  ")
        dict['license']= input("License (MIT) : ")
        dict['readme'] = input("Generate a README.md file ? (y/n)")
        return dict

    def run(self):
        init_dict = self.get_user_infos()
        project = Project(init_dict)
        project.make()
    

""" Project  class"""
class Project():

    def __init__(self,init_dict):
        self.owner_name = init_dict['owner_name'] if init_dict['owner_name'] else '<owner_name>'
        self.owner_email = init_dict['owner_email'] if init_dict['owner_email'] else 'owner_email'
        self.project_name = path.basename(getcwd())
        self.description = init_dict['description']

        self.entry_point = "main.py"
        if init_dict['entry_point'] and re.match(r'.+\.py$',init_dict['entry_point']):
            self.entry_point = init_dict['entry_point']
        
        self.license = "mit"
        if init_dict['license'] and init_dict['license'].lower() in LICENSES :
            self.license = init_dict['license']
        
        self.readme = False
        if init_dict['readme'] and init_dict['readme'].lower() == 'y' :
            self.readme = True

    def make(self):
        # generate license file
        s = Template(LICENSES[self.license]) 
        #replace fields 
        year = time.strftime("%Y")
        license = s.safe_substitute(year=year, name=self.owner_name)
        
        #open new license file and write result
        with open('LICENSE', 'w') as f:
            f.write(license)
        
        #generate readme boilerplate
        readme = Template(README).safe_substitute(project_name=self.project_name, project_description=self.description)
        #open new license file and write result
        with open('README.md', 'w') as f:
            f.write(readme)
        
        

        