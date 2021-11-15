# GenAlgo (Genetic ALGOrithm)

## DEPRECATION NOTICE - UNMAINTAINED

The code in this project was not well coded and too much boilerplate was introduced.
Thus it shall be archived and a new project will see the light, with the goal of being less boilerplate and easier to make evolve

## Installation instructions

Run the following commands to install the requirements:

- First Create a virtuel environment named env
```
python3 -m venv env
```

- Activate it
```
source env/bin/activate
```

- Then update pip within the environment
```
pip install -U pip
```

- Finally install all the requirements recursively
```
pip install -r requirements.txt
```

## Test and calculate coverage

Run coverage to test the code
```
coverage run -m unittest && coverage report
```

For a nicer format, you can run
```
coverage run -m unittest && coverage html
```
