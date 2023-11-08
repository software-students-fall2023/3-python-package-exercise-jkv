[![Python package](https://github.com/software-students-fall2023/3-python-package-exercise-jkv/actions/workflows/python-package.yml/badge.svg)](https://github.com/software-students-fall2023/3-python-package-exercise-jkv/actions/workflows/python-package.yml)

# Team Members
[Jazlene Darrisaw](https://github.com/Jazlene30)

[Haocheng Bai](https://github.com/VincentBai-dotcom)

[Juliann Zhou](https://github.com/juliannzhou)

[Wenqian Li](https://github.com/kevinli2260)


# Project Description
PyMoon is a module that can calculate your moonphase, based on which it gives you life suggestions, compatibility advices, and personality traits.

## Features
* Calculate the moon's phase for a given birth date.
* Determine personality traits associated with specific moon phases.
* Find compatibility based on moon phases.
* Offer life suggestions based on the current moon phase.

## Set Up
First install pipenv if it's not installed on your computer. 

`pip install pipenv`

Then activate the virtual environment and install the dependencies:

`pipenv shell`

`pipenv install`

## Usage:
Once you have installed PyMoon, you can use it in your Python code as follows:

### Get Moon Phase
To calculate the moon phase for a given date, use the following code:
```
from PyMoon.moon_phases import PyMoon

# Get moon phase type
moon_phase = PyMoon.get_type() # # This will prompt for a date input in 'YYYY,MM,DD' format
print(f"Moon Phase: {moon_phase}")
```

### Get personality traits
To determine the personality traits associated with the specific moon phase:
```
personality = PyMoon.get_personality(moon_phase)
print(f"Personality: {personality}")
```
### Get compatibility advice
To determine the personality traits associated with the specific moon phase:
```
compatibility = PyMoon.get_compatibility(moon_phase)
print(f"Compatibility: {compatibility}")
```
### Get life suggestions
For life suggestions based on the current moon phase:
```
life_suggestion = PyMoon.get_life_suggestion(moon_phase)
print(f"Life Suggestion: {life_suggestion}")
```
The output for each function will be returned as a string. 

Moonphase is an enum that could be any one from the list 

`["New Moon",
"Full Moon",
"Waxing Crescent",
"Waning Gibbous",
"First Quarter",
"Third Quarter",
"Waxing Gibbous",
"Waning Crescent"]`



## Testing
To test the functionality of the PyMoon module, navigate to the tests folder and execute the test file using pytest:

`pytest test.py`

## Contributing

Contributions to PyMoon are welcome! Please follow the guidelines below to contribute:

* Fork the repository on GitHub.
* Create a new branch for your improvements (git checkout -b my-improvements).
* Make your changes and commit (git commit -am 'Add some improvements').
* Push to your branch (git push origin my-improvements).
* Submit a pull request through the GitHub website.

We hope you enjoy using PyMoon for your astrological explorations!
