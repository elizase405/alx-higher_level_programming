#!/usr/bin/python3

"""
A module with 1 function
"""


class MyList(list):
    """ Class that inherits the attributes references of class list

    Args:
        list: class list

    """

    def print_sorted(self):
        """
        Method that prints the sorted list

        Args: None

        Raises: None
        """

        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
