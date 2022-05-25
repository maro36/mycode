#!/usr/bin/python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


for farm in farms:
        #print(farm)   # this might be a good "first step" after developing the loop
        print(farm.get("name", "Unknown Farm"), end=":\n")  # this is like saying, "farm['name']"
                                                 # only it will not return an error
        for agri in farm.get("agriculture"):   
            print("  -", agri)
