[![Python package](https://github.com/software-students-fall2023/3-python-package-exercise-jkv/actions/workflows/python-package.yml/badge.svg)](https://github.com/software-students-fall2023/3-python-package-exercise-jkv/actions/workflows/python-package.yml)

# Description
PyMoon is a module that can calculate your moonphase, based on which it gives you life suggestions, compatibility advices, and personality traits.

To use:

`from moon_phases import PyMoon`

`PyMoon.get_type()`

`PyMoon.get_personality(moonphase)`

`PyMoon.get_compatibility(moonphase)`

`PyMoon.get_life_suggestion(moonphase)`

Output will be returned as strings

Moonphase is an enum that could be any one from the list 

`["New Moon",
"Full Moon",
"Waxing Crescent",
"Waning Gibbous",
"First Quarter",
"Third Quarter",
"Waxing Gibbous",
"Waning Crescent"]`

# Set Up
First install pipenv if it's not installed on your computer. 

`pip install pipenv`

Then activate the virtual environment and install the dependencies:

`pipenv shell`

`pipenv install`

# Testing
Go to the tests folder and run 

`pytest test.py`
