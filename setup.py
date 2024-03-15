from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A simple Python package for crowd behavior modeling'
LONG_DESCRIPTION = 'A simple Python model for understanding crowd behaviour at peak times in different situations, such as evacuating a room, moving through a crowded corridor, or managing demonstrations'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="crowdMo",
        version=VERSION,
        author="Samadou Ouro-agorouko",
        author_email="<souroagorouko@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['numpy', 'matplotlib'], # additional packages that 
        # needs to be installed along with this package.

        keywords=['python', 'Crowd behavio Modelisation'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)