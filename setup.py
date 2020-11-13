from setuptools import setup, find_packages

setup(
    name='lazylister',
    version='1.0.1',
    license='MIT',
    description='A cute little lister script that literally just returns a list of each line in a file.',
    author='James Scheiber',
    author_email='jscheiber22@gmail.com',
    url="https://github.com/jscheiber22/lazylister",
    packages=find_packages(include=['lazylister', 'lazylister.*'])
)
