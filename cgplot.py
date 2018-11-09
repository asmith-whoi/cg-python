"""
Standardized plotting functions.
"""

import matplotlib.pyplot as plt

def cgplotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.

    Paramaters:
    ax (axes): The axes to draw

    data1 (array): The x data

    data2 (array): The y data

    param_dict (dictionary): Dictionary of kwargs to pass to ax.plot

    Returns:
    list of artists added
    """

    return ax.plot(data1, data2, **param_dict)

