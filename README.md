# Code handouts for TTK4130 - Modelling and simulation

Welcome to the TTK4130 code-handout repository.
This is a companion repository to the assignments on the course website and holds Jupyter notebooks for all the assignments where you are expected to finish some already existing code.

There is one notebook for each relevant assignment:

- Assignment 5, Satellite, `satellite.ipynb`
  - Relevant assignment: https://ttk4130.github.io/assignments/assignment-5.html
- Assignment 6, Ball and Beam, `ball-and-beam.ipynb`
  - Relevant assignment: https://ttk4130.github.io/assignments/assignment-6.html
- Assignment 7, Hovering Mass, `hovering-mass.ipynb`
  - Relevant assignment: https://ttk4130.github.io/assignments/assignment-7.html
- Assignment 9, Car Simulation, `car.ipynb`
  - Relevant assignment: https://ttk4130.github.io/assignments/assignment-9.html

## How to run

Clone the repo, launch your favorite jupyter notebook server and run the notebook!
See the [Python installation guide](https://ttk4130.github.io/installation.html)
and the  [quick introduction to Jupyter Notebook](https://ttk4130.github.io/jupyter-notebook.html)
for more information and some tips.

## Dependencies

The dependencies in this repositiory are defined in `pixi.toml`.
In addition to the `toml`-file, we have included a script that tests the dependencies.
The primary reason for having package managers and virtual environment managers like pixi is to specify and synchronize dependencies across contributors and time.
In a sense, the dependency test script we have included is also a rudimentary way of achieving this.
We have only included the script for pedagogical reasons, namely so you can check whether you've installed pixi correctly and so on.
