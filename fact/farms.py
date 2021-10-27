#!/usr/bin/env python3

## Farm and Animals Details 

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for NE_ANIMALS in farms:
    if (NE_ANIMALS["name"])=="NE Farm":
        print("the NE Animals are :", NE_ANIMALS["agriculture"])
for animal in farms:
        farm= input("What is your Favourite FArm NE , W ,SE ?\n>")
        print ( "The  Animals in your favourite farm " + farm + "is")
        if(farm=="NE"):
            print("sheep", "cows", "pigs", "chickens", "llamas", "cats")
        elif(farm=="W"):
            print("pigs", "chickens", "llamas")
            elif(farm=="SE"):
                print("chickens", "carrots", "celery")


