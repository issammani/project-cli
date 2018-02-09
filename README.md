# Project-cli [![Build Status](https://travis-ci.org/issamouu69/project-cli.svg?branch=master)](https://travis-ci.org/issamouu69/project-cli)
    simple utility to create basic structure of python projet.
## Installation
For now just clone the directory and run setup.py like so :
```bash
git clone https://github.com/issamouu69/project-cli.git
cd project_cli
python setup.py install # For now supporting python3 only
```
## Running application
For convenience, you have to set two variables (one time only) before running the utility.
Execute the commands below in your terminal : 
For Linux/Mac :
```bash
echo 'export PROJECT_OWNER_NAME="Issam Mani";' >> ~/.bashrc # change with your name
echo 'export PROJECT_OWNER_EMAIL="issamouu69@gmail.com";' >> ~/.bashrc # change with your email
```

For Windows :
```bash
SETX PROJECT_OWNER_NAME="Issam Mani" &:: change with your name
SETX PROJECT_OWNER_EMAIL="issamouu69@gmail.com" &:: change with your email
```

Now you are all set , just navigate to the directory you want to generate the files :
```bash
$ project init
``` 
## License

Apache 2.0. See [/LICENSE](/LICENSE)