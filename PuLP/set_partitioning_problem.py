"""
A set partitioning model of a wedding seating problem

Authors: Stuart Mitchell 2009
"""
from typing import Tuple, Union
import pulp as lp

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
possible_tables = [tuple(i) for i in lp.allcombinations(guests, max_table_size)]

#create the problem
seating_chart = lp.LpProblem('Set Partitioning', lp.LpMinimize)

#create binary variable: 1 if table is in final solution, 0 if not
table_chart = ['_'.join(i) for i in possible_tables] #changes tuples to strings
var_keys = lp.LpVariable.dicts('table_%s', table_chart, 0, 1, lp.LpInteger) #creates Lp vars for each table
x = {i: var_keys['_'.join(i)] for i in possible_tables} #creates dict with tuples as keys and Lp vars as values

#add objective function: maximize happiness
seating_chart += lp.lpSum(happiness(table) * x[table] for table in possible_tables), 'Total Happiness'

#add constraints
seating_chart += lp.lpSum(x[table] for table in possible_tables) <= max_tables, 'Max Tables'
for guest in guests:
    seating_chart += lp.lpSum([x[table] for table in possible_tables if guest in table]) == 1, f'{guest} is seated at only one table'

#solve by running the model
seating_chart.writeLP('set_partitioning_problem.lp')
seating_chart.solve()

#print results
print('Status =', lp.LpStatus[seating_chart.status])
print('Max happiness =', lp.value(seating_chart.objective))
for table in possible_tables:
    if x[table].value() == 1:
        print(table)