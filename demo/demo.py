import numpy as np


def add_numbers(x, y):
    """Add two integers."""
    return x + y


def multiply_numbers(x, y):
    """Multiply two integers."""
    return x * y


def generate_random():
    """Generate random number."""
    return np.random


def fail_security_func():
    """A badly written function to be highlighted."""
    try:
        x = 1 + 1
    except Exception as e:
        pass
    return x
