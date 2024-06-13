from setuptools import setup, find_packages

setup(
    name='sudoku-solver',
    version='0.1.0',
    description='A python based sudoku solver',
    url='https://github.com/countertorque/sudoku-solver',
    author='Matt Hartfield',
    author_email='hartfield-sudoku@gmail.com',
    license='Apache2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'sudoku-solver = sudoku-solver.cli:cli',
        ],
    },
)