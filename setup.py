
# setup.py
from setuptools import setup
from setuptools import find_packages


with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='goalguru',
      #version="0.0.7" <insert version>,
      description="goalguru Model",
      license="MIT" , ## Es para poner una licencia al modelo. MIT: es para publicos,
      #author="Javier, Juan y Sebastian",
      ##author_email="contact@lewagon.org" <Insert authors email>,
      #url="https://github.com/jotanavarrete/goalguru",
      install_requires=requirements,
      packages=find_packages(),
      #test_suite="tests",
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
