def area(a, b):
    """
    Args:
        a:
        b:
    """
    return a * b


# Non-Keyword/ Positional Arguments
print(area(4, 5))
# Keyword Arguments
print(area(b=5, a=4))


# Functions with an arbitrary number of non-keywords
def mean(*args):
    """
    Args:
        *args:
    """
    return args


print(mean(1, 2, 'a', 4))


def mean2(*args):
    """
    Args:
        *args:
    """
    return sum(args) / len(args)


print(mean2(1, 2, 3, 4))

# Functions with arbitrary number of keyword arguments
"""
kwargs = Keyword Arguments
"""


def mean3(**kwargs):
    """
    Args:
        **kwargs:
    """
    return kwargs


print(mean3(x=4, b=10, z=3))
