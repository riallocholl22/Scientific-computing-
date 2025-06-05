import numpy as np
from scipy import integrate

# Define the function for the surface
def surface_function(x, y):
    return x**2 + y**2

# Compute the volume under the surface over the region 0 <= x, y <= 1
volume, error = integrate.dblquad(surface_function, 0, 1, lambda x: 0, lambda x: 1)
print(f'Volume under the surface: {volume:.4f}')
