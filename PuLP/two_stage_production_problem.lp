\* Two_Stage_Production_Problem *\
Maximize
Total_profit: 25 scenario_0_pliers + 40 scenario_0_wrenches
 + 25 scenario_1_pliers + 40 scenario_1_wrenches + 25 scenario_2_pliers
 + 22.5 scenario_2_wrenches + 25 scenario_3_pliers + 22.5 scenario_3_wrenches
 - 58 steel_purchase
Subject To
Assembly_cap_in_scen_0: 0.5 scenario_0_pliers + 0.3 scenario_0_wrenches <= 8
Assembly_cap_in_scen_1: 0.5 scenario_1_pliers + 0.3 scenario_1_wrenches <= 10
Assembly_cap_in_scen_2: 0.5 scenario_2_pliers + 0.3 scenario_2_wrenches <= 8
Assembly_cap_in_scen_3: 0.5 scenario_3_pliers + 0.3 scenario_3_wrenches <= 10
Max_production_in_scen_0_for_pliers: scenario_0_pliers <= 16
Max_production_in_scen_0_for_wrenches: scenario_0_wrenches <= 15
Max_production_in_scen_1_for_pliers: scenario_1_pliers <= 16
Max_production_in_scen_1_for_wrenches: scenario_1_wrenches <= 15
Max_production_in_scen_2_for_pliers: scenario_2_pliers <= 16
Max_production_in_scen_2_for_wrenches: scenario_2_wrenches <= 15
Max_production_in_scen_3_for_pliers: scenario_3_pliers <= 16
Max_production_in_scen_3_for_wrenches: scenario_3_wrenches <= 15
Molding_hours_in_scen_0: scenario_0_pliers + scenario_0_wrenches <= 21
Molding_hours_in_scen_1: scenario_1_pliers + scenario_1_wrenches <= 21
Molding_hours_in_scen_2: scenario_2_pliers + scenario_2_wrenches <= 21
Molding_hours_in_scen_3: scenario_3_pliers + scenario_3_wrenches <= 21
Steel_used_in_scen_0: scenario_0_pliers + 1.5 scenario_0_wrenches
 - steel_purchase <= 0
Steel_used_in_scen_1: scenario_1_pliers + 1.5 scenario_1_wrenches
 - steel_purchase <= 0
Steel_used_in_scen_2: scenario_2_pliers + 1.5 scenario_2_wrenches
 - steel_purchase <= 0
Steel_used_in_scen_3: scenario_3_pliers + 1.5 scenario_3_wrenches
 - steel_purchase <= 0
End
