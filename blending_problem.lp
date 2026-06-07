\* Blending *\
Minimize
Total_cost_of_ingredients_per_can: 0.008 ingr_Beef + 0.013 ingr_Chicken
 + 0.001 ingr_Gel + 0.01 ingr_Mutton + 0.002 ingr_Rice + 0.005 ingr_Wheat
Subject To
Fat_>=_6g: 0.1 ingr_Beef + 0.08 ingr_Chicken + 0.11 ingr_Mutton
 + 0.01 ingr_Rice + 0.01 ingr_Wheat >= 6
Fibre_<=_2g: 0.005 ingr_Beef + 0.001 ingr_Chicken + 0.003 ingr_Mutton
 + 0.1 ingr_Rice + 0.15 ingr_Wheat <= 2
Protein_>=_8g: 0.2 ingr_Beef + 0.1 ingr_Chicken + 0.15 ingr_Mutton
 + 0.04 ingr_Wheat >= 8
Salt_<=_0.4g: 0.005 ingr_Beef + 0.002 ingr_Chicken + 0.007 ingr_Mutton
 + 0.002 ingr_Rice + 0.008 ingr_Wheat <= 0.4
Total_ingredients_=_100g: ingr_Beef + ingr_Chicken + ingr_Gel + ingr_Mutton
 + ingr_Rice + ingr_Wheat = 100
End
