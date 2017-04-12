# OpenTIRE - The open-source mathematical tire modelling library

The OpenTire project is a non-commercial project that has three primary goals:
* Provide a library of open-source tire models in an easily accessible and useable format
* Provide a technical platform for collaborative tire model development
* Build a library of tire data and tire models available for use in research projects
 
## Background
The complexity involved in simulating tires can make it difficult to implement tire models in research and development studies. Firstly, turning equations in literature into software code can be a daunting task. Testing and validating an implementation is difficult and time consuming. Secondly, without a single open-source implementation of tire models collaborative development of tire models are difficult and slow. Lastly, getting access to tire data and tire models without large investments in testing is very difficult. As a result a significant part of tire and vehicle dynamics research is carried out using a tire model for 205/60R15 tire, which is readily available in literature.

## Getting Started
If you are unfamiliar with packages and modules in Python, the first thing you'll have to do before using OpenTire is to install the package with your Python installation. To help with this, OpenTire comes with a setup scripts that automates it all. To install it, run the setup.py script with install as an argument.

```python
setup.py install
```
Once OpenTire is installed, you can load up a tire model with these commands:

```python
from opentire import OpenTire
from opentire.Core import TireState

openTire = OpenTire()
myTireModel = openTire.createmodel('PAC2002')

state = TireState()
state['FZ'] = 1500
state['IA'] = 0.0
state['SR'] = 0.0
state['SA'] = 0.0
state['FY'] = 0.0
state['V'] = 10.0
state['P'] = 260000

myTireModel.solve(state)
```

For more comprehensive examples, please check out the additional examples in the examples folder.

## Examples
To help you get started using OpenTire, there are a number of different Jupyter Notebooks which demonstrates how to initiate OpenTire and how to integrate into a tire or vehicle simulation.

## More info
Existing tire model implementations are generally built on dated programming languages which make integration with modern software tools difficult and inefficient. By utilizing a modern open-source scientific programming language (Python) along with modern collaborative tools (online code repositories) the threshold for entry into developing and utilizing tire models is significantly lowered. 

## Development plan
The first release includes implementations of commonly used tire models along with implementation examples, benchmark studies and the first library of parameterized tire models.

Since the project start in late 2014, the project has received support from both academic and commercial contributors. More contributors are wanted to help define the roadmap for future development.
