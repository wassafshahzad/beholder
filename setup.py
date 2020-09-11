from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='be_holder',
      version='1.1',
      description='A python module for type checking function parameters and returns',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/wassafshahzad/beholder',
      author='Wassaf Shahzad',
      author_email='wassafshahzad@gmail.com',
      license='MIT',
      packages=['beholder'],
      zip_safe=False)
