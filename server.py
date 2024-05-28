import requests



#print(requests.get("http://localhost:8008/items/1").json())

# A POST request to tthe API
"""
parameters = {   
                "user_id": "damir_on",
                "year": 1980,
                "month":7, 
                "date": 6,
                "local_time": 2.0, # sätt klockan - 1 timme 1 aprill till sista oktober 
                "longi": 18.063326,
                "lati": 59.300866,
                "hours_difference":1,
                "gender":'male',
                "exact_time":False
              }
 """

parameters = {   
                "user_id": "samsam",
                "year": 1980,
                "month":7, 
                "date": 10,
                "local_time": 16.00, # sätt klockan - 1 timme 1 aprill till sista oktober 
                "longi": 18.063326,
                "lati": 59.300866,
                "hours_difference":1,
                "gender":'male',
                "exact_time":False
              }
resp = requests.post("http://localhost:8008/user_info/newuser", json=parameters).json()

#parameters = {"username":"Stefan atlas1234"}
#resp = requests.post("http://localhost:8008/database/newuser", json=parameters)

print(resp)

#print(resp.json())

#parameters = {"id": 2, "name":"stefan", "price":1, "count":2,  }
#print(requests.post("http://localhost:8008/items/i", json=parameters).json())
#print(requests.get("http://localhost:8008/database/", json=parameters).json())

#print(requests.get("http://localhost:8008/items").json())






#År	Sommartid börjar	Sommartid slutar
#–1915	Ingen sommartid
#1916	15 maj	30 september[5]
#1917–1979	Ingen sommartid
#1980	Första söndagen i april	Sista söndagen i september
#1981–1995	Sista söndagen i mars	Sista söndagen i september
#1996–	Sista söndagen i mars	Sista söndagen i oktober





