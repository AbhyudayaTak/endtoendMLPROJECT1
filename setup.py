from setuptools import find_packages,setup
from typing import List
hypen_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
       this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements ]
        
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements



setup(
name= 'mlproject',
version='0.0.1',
author='Abhyudaya',
author_email='abyudayatak@gmail.com',
packages=find_packages(), # ye dhoondega kitne folder mai aapne __init__.py file bana rkhi hai yaa nhi, toh uss folder ko 
# apne aap package maan lega
# install_requires=['pandas','numpy','seaborn']
# but humey agar 100+ packages chaiye toh aise ek ek likhna toh fesiable nhi hai toh hum ek function banaenge :-
install_requires=get_requirements('requirements.txt')
)
