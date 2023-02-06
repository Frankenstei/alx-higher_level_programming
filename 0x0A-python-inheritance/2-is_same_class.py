#!use/bin/python3
"""checks if object is similar to class"""
def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
