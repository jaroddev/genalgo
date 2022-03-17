# GenAlgo (Genetic ALGOrithm)

## DEPRECATION NOTICE - UNMAINTAINED

This project was moved to another repository. Indeed, the design of the application was not fitting the actual needs.
It was split into two projects, projects you can find at those URLs:
 - https://github.com/jaroddev/evolugo
 - https://github.com/jaroddev/evotest

Evolugo is the micro-framework/library part, to implement a genetic algorithm.
Evotest is an implementation example of a problem with evolugo, the Onemax problem, 
it also contains few resources to do some benchmarks.

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
