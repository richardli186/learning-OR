"""
Transportation Problem 2

Warehouses (supply):
Chicago:     400 units
Dallas:      300 units
Seattle:     500 units

Stores (demand):
New York:    350 units
Miami:       250 units
Denver:      200 units
LA:          300 units

Shipping cost per unit:
             New York   Miami   Denver    LA
Chicago         3         5       4       7
Dallas          6         3       2       5
Seattle         8         7       3       2

Objective: Minimize total shipping cost

Constraints:
Chicago ships <= 400 total
Dallas ships <= 300 total
Seattle ships <= 500 total
New York receives >= 350
Miami receives >= 250
Denver receives >= 200
LA receives >= 300
All shipments >= 0 and integers
"""
import pulp as lp

prob = lp.LpProblem('Transportation Problem', lp.LpMinimize)

warehouses = ['Chicago', 'Dallas', 'Seattle']
stores = ['New York', 'Miami', 'Denver', 'LA']

costs = [
    [3, 5, 4, 7], #Chicago
    [6, 3, 2, 5], #Dallas
    [8, 7, 3, 2] #Seattle
]

supply = {'Chicago': 400, 'Dallas': 300, 'Seattle': 500}
demand = {'New York': 350, 'Miami': 250, 'Denver': 200, 'LA': 300}

routes = [(w, s) for w in warehouses for s in stores] #all possible routes

costs_dict = lp.makeDict([warehouses, stores], costs, 0)

#create Lp vars
lp_routes = lp.LpVariable.dicts('Route', (warehouses, stores), 0, None, lp.LpContinuous)

#add objective function: lowest total shipping cost
prob += lp.lpSum(costs_dict[w][s] * lp_routes[w][s] for (w, s) in routes), 'Total shipping cost'

#add contraints
for w in warehouses:
    prob += lp.lpSum(lp_routes[w][s] for s in stores) <= supply[w], f'Supplied from {w}'

for s in stores:
    prob += lp.lpSum(lp_routes[w][s] for w in warehouses) >= demand[s], f'Received by {s}'

#write and solve problem
prob.writeLP('blind_transport_prob.lp')
prob.solve()

#print results
print('Status =', lp.LpStatus[prob.status])
#for var in prob.variables():
    #print(var.name, '=', lp.value(var))
print('Total shipping cost =', lp.value(prob.objective))

#put info into table
print(f"{'From':<12} {'To':<12} {'Units':>8}")
print("-" * 34)
for w in warehouses:
    for s in stores:
        val = lp.value(lp_routes[w][s])
        if val > 0:
            print(f"{w:<12} {s:<12} {val:>8.0f}")