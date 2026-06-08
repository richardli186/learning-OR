"""
Two Stage Production Planning Problem

Products: wrenches, pliers
Steel per unit: wrenches: 1.5, pliers: 1
Molding per unit: wrenches: 1, pliers: 1
Assembly per unit: wrenches: 0.3, pliers: 0.5
Steel price: 58
Steel capacity: 27
Molding capacity: 21
Max demand: wrenches: 15, pliers: 16

Scenarios (probability 0.25 each):

scenario 0: wrench earnings = 160, plier earnings = 100, assembly cap = 8
scenario 1: wrench earnings = 160, plier earnings = 100, assembly cap = 10
scenario 2: wrench earnings = 90,  plier earnings = 100, assembly cap = 8
scenario 3: wrench earnings = 90,  plier earnings = 100, assembly cap = 10
Objective: Maximize expected net revenue minus steel purchase cost

Constraints:

steel used per scenario <= steel purchased
molding hours per scenario <= 21
assembly hours per scenario <= scenario assembly cap
production per product per scenario <= max demand
all variables >= 0
"""
import pulp as lp

products = ["wrenches", "pliers"]
steel_per_unit = [1.5, 1]
molding_per_unit = [1, 1]
assembly_per_unit = [0.3, 0.5]
steel_price = 58
steel_capacity = 27
molding_capacity = 21
max_demand = [15, 16]

scenarios = [0, 1, 2, 3]
pscenario = [0.25, 0.25, 0.25, 0.25]
wrench_earnings = [160, 160, 90, 90]
plier_earnings = [100, 100, 100, 100]
assembly_capacity = [8, 10, 8, 10]

#create representations of each scenario for each product
production_scen = [(scen, prod) for scen in scenarios for prod in products]
scen_earnings = [[wrench_earnings[i], plier_earnings[i]] for i in scenarios]
item_earnings = [item for sublist in scen_earnings for item in sublist]

#create dicts for each scenario and factor
steel_pu_dict = dict(zip(products, steel_per_unit))
molding_pu_dict = dict(zip(products, molding_per_unit))
assembly_pu_dict = dict(zip(products, assembly_per_unit))
earnings_dict = dict(zip(production_scen, item_earnings))
max_demand_dict = dict(zip(products, max_demand))

#create the problem
prob = lp.LpProblem('Two Stage Production Problem', lp.LpMaximize)

#create the vars
steel_purchase = lp.LpVariable('steel purchase', 0, None, lp.LpContinuous)
production_vars = lp.LpVariable.dicts('scenario', (scenarios, products), 0, None, lp.LpContinuous)

#add objective function: maximum profit
prob += lp.lpSum(
    pscenario[i] * (earnings_dict[(i, j)] * production_vars[i][j]) for i, j in production_scen
    ) - steel_purchase * steel_price, 'Total profit'

#add constraints for each scenario
for i in scenarios:
    prob += lp.lpSum(production_vars[i][j] * steel_pu_dict[j] for j in products) - steel_purchase <= 0, f'Steel used in scen {i}'
    prob += lp.lpSum(production_vars[i][j] * molding_pu_dict[j] for j in products) - molding_capacity <= 0, f'Molding hours in scen {i}'
    prob += lp.lpSum(production_vars[i][j] * assembly_pu_dict[j] for j in products) - assembly_capacity[i] <= 0, f'Assembly cap in scen {i}'
    for j in products:
        prob += production_vars[i][j] - max_demand_dict[j] <= 0, f'Max production in scen {i} for {j}'

#write the problem and solve
prob.writeLP('two_stage_production_problem.lp')
prob.solve()

#print results
print('Status =', lp.LpStatus[prob.status])
for var in prob.variables():
    print(var.name, '=', lp.value(var))
print('Steel to buy =', lp.value(prob.objective))