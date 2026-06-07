"""
Transportation Problem Practice

Warehouses (supply nodes):
    A: 1000 cases, B: 4000 cases

Bars (demand nodes):
    1: 500 cases, 2: 900 cases, 3: 1800 cases, 4: 200 cases, 5: 700 cases

Costs (dollars per crate):
        Bar1  Bar2  Bar3  Bar4  Bar5
    A    2     4     5     2     1
    B    3     1     3     2     3
Objective: Minimize total transportation cost

Constraints:
    A ships ≤ 1000 total
    B ships ≤ 4000 total
    Bar 1 receives ≥ 500
    Bar 2 receives ≥ 900
    Bar 3 receives ≥ 1800
    Bar 4 receives ≥ 200
    Bar 5 receives ≥ 700
    All shipments ≥ 0 and must be integers
"""
import pulp as lp

warehouses = ['A', 'B']

bars = ['1', '2', '3', '4', '5']

costs = [
    [2, 4, 5, 2, 1], #A
    [3, 1, 3, 2, 3] #B
]

supply = {'A': 1000, 'B': 4000}

demand = {'1': 500, '2': 900, '3': 1800, '4': 200, '5': 700}

#create the problem
prob = lp.LpProblem('Transportation Problem', lp.LpMinimize)

#create dict from cost values
costs_dict = lp.makeDict([warehouses, bars], costs, 0)

#create list of all possible routes
routes = [(w, b) for w in warehouses for b in bars]

#create Lp variables. passing mult lists creates nested dict
vars_dict = lp.LpVariable.dicts('Route', (warehouses, bars), 0, None, lp.LpInteger)
print(list(vars_dict.keys())[:3])

#add objective function: minimize total transportation cost
prob += lp.lpSum(vars_dict[w][b] * costs_dict[w][b] for (w, b) in routes), 'Total transportation cost'

#add constraints
for w in warehouses:
    prob += lp.lpSum(vars_dict[w][b] for b in bars) <= supply[w], f'{w} supply'

for b in bars:
    prob += lp.lpSum(vars_dict[w][b] for w in warehouses) >= demand[b], f'{b} demand'

#write the problem and solve
prob.writeLP('transportation_problem.lp')
prob.solve()

#print results
print('Status =', lp.LpStatus[prob.status])
for var in prob.variables():
    print(var.name, '=', lp.value(var))
print('Lowest cost =', lp.value(prob.objective))