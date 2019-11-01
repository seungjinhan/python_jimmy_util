from setuptools import setup, find_packages
  
 
setup(name='jimmy_util',
 
      version='0.1.6',
 
      url='https://github.com/seungjinhan/python_packages',
 
      license='MIT',
 
      author='jimmyhan',
 
      author_email='hanblues@gmail.com',
 
      description='python utils - 날짜 util 추가',
 
      packages=find_packages(),
 
      long_description=open('README.md').read(),
 
      zip_safe=False,
)