"""
A set partitioning model of a wedding seating problem

Authors: Stuart Mitchell 2009
"""
from typing import Tuple, Union
from pulp import *

max_tables = 5
max_table_size = 4
guests = "A B C D E F G I J K L M N O P Q R".split()

def happiness(
    table: Union[
        Tuple[str, str], Tuple[str, str, str, str], Tuple[str], Tuple[str, str, str]
    ],
) -> int:
    """
    Find the happiness of the table
    - by calculating the maximum distance between the letters
    """
    return abs(ord(table[0]) - ord(table[-1]))

#create list of all possible tables
possible_tables = [tuple(i) for i in allcombinations(guests, max_table_size)]

#create the problem
seating_chart = LpProblem()

#create binary variable: 1 if table is in final solution, 0 if not
