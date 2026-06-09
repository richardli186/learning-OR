\* Transportation_Problem *\
Minimize
Total_shipping_cost: 4 Route_Chicago_Denver + 7 Route_Chicago_LA
 + 5 Route_Chicago_Miami + 3 Route_Chicago_New_York + 2 Route_Dallas_Denver
 + 5 Route_Dallas_LA + 3 Route_Dallas_Miami + 6 Route_Dallas_New_York
 + 3 Route_Seattle_Denver + 2 Route_Seattle_LA + 7 Route_Seattle_Miami
 + 8 Route_Seattle_New_York
Subject To
Received_by_Denver: Route_Chicago_Denver + Route_Dallas_Denver
 + Route_Seattle_Denver >= 200
Received_by_LA: Route_Chicago_LA + Route_Dallas_LA + Route_Seattle_LA >= 300
Received_by_Miami: Route_Chicago_Miami + Route_Dallas_Miami
 + Route_Seattle_Miami >= 250
Received_by_New_York: Route_Chicago_New_York + Route_Dallas_New_York
 + Route_Seattle_New_York >= 350
Supplied_from_Chicago: Route_Chicago_Denver + Route_Chicago_LA
 + Route_Chicago_Miami + Route_Chicago_New_York <= 400
Supplied_from_Dallas: Route_Dallas_Denver + Route_Dallas_LA
 + Route_Dallas_Miami + Route_Dallas_New_York <= 300
Supplied_from_Seattle: Route_Seattle_Denver + Route_Seattle_LA
 + Route_Seattle_Miami + Route_Seattle_New_York <= 500
End
