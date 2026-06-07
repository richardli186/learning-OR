\* Transportation_Problem *\
Minimize
Total_transportation_cost: 2 Route_A_1 + 4 Route_A_2 + 5 Route_A_3
 + 2 Route_A_4 + Route_A_5 + 3 Route_B_1 + Route_B_2 + 3 Route_B_3
 + 2 Route_B_4 + 3 Route_B_5
Subject To
1_demand: Route_A_1 + Route_B_1 >= 500
2_demand: Route_A_2 + Route_B_2 >= 900
3_demand: Route_A_3 + Route_B_3 >= 1800
4_demand: Route_A_4 + Route_B_4 >= 200
5_demand: Route_A_5 + Route_B_5 >= 700
A_supply: Route_A_1 + Route_A_2 + Route_A_3 + Route_A_4 + Route_A_5 <= 1000
B_supply: Route_B_1 + Route_B_2 + Route_B_3 + Route_B_4 + Route_B_5 <= 4000
Bounds
 0 <= Route_A_1
 0 <= Route_A_2
 0 <= Route_A_3
 0 <= Route_A_4
 0 <= Route_A_5
 0 <= Route_B_1
 0 <= Route_B_2
 0 <= Route_B_3
 0 <= Route_B_4
 0 <= Route_B_5
Generals
Route_A_1
Route_A_2
Route_A_3
Route_A_4
Route_A_5
Route_B_1
Route_B_2
Route_B_3
Route_B_4
Route_B_5
End
