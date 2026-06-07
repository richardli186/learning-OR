"""
Whiskas Blending Problem - Practice

Costs (per gram):
    Chicken: 0.013, Beef: 0.008, Mutton: 0.010, Rice: 0.002, Wheat: 0.005, Gel: 0.001

Protein percent:
    Chicken: 0.100, Beef: 0.200, Mutton: 0.150, Rice: 0.000, Wheat: 0.040, Gel: 0.000

Fat percent:
    Chicken: 0.080, Beef: 0.100, Mutton: 0.110, Rice: 0.010, Wheat: 0.010, Gel: 0.000

Fibre percent:
    Chicken: 0.001, Beef: 0.005, Mutton: 0.003, Rice: 0.100, Wheat: 0.150, Gel: 0.000

Salt percent:
    Chicken: 0.002, Beef: 0.005, Mutton: 0.007, Rice: 0.002, Wheat: 0.008, Gel: 0.000

Requirements:
    All ingredients must sum to 100g
    Protein ≥ 8.0
    Fat ≥ 6.0
    Fibre ≤ 2.0
    Salt ≤ 0.4
"""
import pulp as lp

ingredients = ['Chicken', 'Beef', 'Mutton', 'Rice', 'Wheat', 'Gel']

cost = {
    'Chicken' : 0.013, 
    'Beef' : 0.008,
    'Mutton' : 0.010, 
    'Rice': 0.002, 
    'Wheat': 0.005, 
    'Gel': 0.001
}

protein = {
    'Chicken': 0.100,
    'Beef': 0.200, 
    'Mutton': 0.150, 
    'Rice': 0.000, 
    'Wheat': 0.040, 
    'Gel': 0.000
}

fat = {
    'Chicken': 0.080, 
    'Beef': 0.100, 
    'Mutton': 0.110, 
    'Rice': 0.010, 
    'Wheat': 0.010, 
    'Gel': 0.000
}

fibre = {
    'Chicken': 0.001, 
    'Beef': 0.005, 
    'Mutton': 0.003, 
    'Rice': 0.100, 
    'Wheat': 0.150, 
    'Gel': 0.000
}

salt = {
    'Chicken': 0.002, 
    'Beef': 0.005, 
    'Mutton': 0.007, 
    'Rice': 0.002, 
    'Wheat': 0.008, 
    'Gel': 0.000
}

#create the problem
prob = lp.LpProblem("Blending", lp.LpMinimize) 

#create dict of Lp vars, instead of one by one
ingredient_vars = lp.LpVariable.dicts('ingr', ingredients, 0, None, lp.LpContinuous)

#add objective function: lowest cost
prob += lp.lpSum(cost[i] * ingredient_vars[i] for i in ingredients), 'Total cost of ingredients per can'

#add constraints
prob += lp.lpSum(ingredient_vars[i] for i in ingredients) == 100, 'Total ingredients = 100g',
prob += lp.lpSum(protein[i] * ingredient_vars[i] for i in ingredients) >= 8, 'Protein >= 8g'
prob += lp.lpSum(fat[i] * ingredient_vars[i] for i in ingredients) >= 6, 'Fat >= 6g'
prob += lp.lpSum(fibre[i] * ingredient_vars[i] for i in ingredients) <= 2, 'Fibre <= 2g'
prob += lp.lpSum(salt[i] * ingredient_vars[i] for i in ingredients) <= 0.4, 'Salt <= 0.4g'

#solve by running the model
prob.writeLP('blending_problem.lp')
prob.solve()

#print results
print('Status =', lp.LpStatus[prob.status])
for var in prob.variables():
    print(var.name, '=', var.varValue)
print('Total cost per can =', lp.value(prob.objective))