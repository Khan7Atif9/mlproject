from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requierments=[]
    with open(file_path) as file_obj:
        requierments=file_obj.readlines()
        requierments=[req.replace("\n","") for req in requierments]

        if HYPEN_E_DOT in requierments:
            requierments.remove(HYPEN_E_DOT)

    return requierments    

    

setup(
    name='mlproject',
    version='0.0.1',
    author='Atif',
    author_email='atiifkhhann@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)