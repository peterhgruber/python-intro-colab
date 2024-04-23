# myfunctions - a simple Python module
# peter.gruber@usi.ch, 2024-04
# See here: https://github.com/peterhgruber/python-intro-colab
# Functions from: https://github.com/peterhgruber/python-intro-colab/blob/main/02Python_Functions.ipynb

def f(x):
    return x**2 - 2*x + 1

def unif_dens(x,a,b):
    # Case 1: x is outside the interval
    if x < a or x > b:
        return 0
    # Case 2: x is inside the interval
    else:
        return 1/(b-a)