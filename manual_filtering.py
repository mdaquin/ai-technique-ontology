import json
import os.path
import random
import sys
import config

all_entities = {}
with open("data/entities.json") as f:
    all_entities = json.load(f)

y_entities = {}
if os.path.isfile("data/y_entities.json"):
    with open("data/y_entities.json") as f:
        y_entities = json.load(f)

n_entities = {}
if os.path.isfile("data/n_entities.json"):
    with open("data/n_entities.json") as f:
        n_entities = json.load(f)    

u_entities = {}
if os.path.isfile("data/u_entities.json"):
    with open("data/u_entities.json") as f:
        u_entities = json.load(f)    

alreadydone = []
for i in y_entities:
    alreadydone.append(i)
for i in n_entities:
    alreadydone.append(i)
for i in u_entities:
    alreadydone.append(i)
    
todo = []
for i in all_entities:
    if i not in alreadydone:
        todo.append(i)

while len(todo) > 0:
    i = random.randint(0,len(todo)-1)
    e = todo.pop(i)
    if "label" in all_entities[e]:
        try:
            answer = raw_input("Is https://www.wikidata.org/wiki/"+e+" - "+all_entities[e]["label"]+" relevant to "+all_entities[config.eid]["label"]+"?\n y(es) - n(o) - u(nsure) - q(uit)\n")
            if answer == "q": sys.exit()
            if answer == "y":
                y_entities[e] = all_entities[e]
                with open('data/y_entities.json', 'w') as outfile:
                    json.dump(y_entities, outfile)
            if answer == "n":
                n_entities[e] = all_entities[e]
                with open('data/n_entities.json', 'w') as outfile:
                    json.dump(n_entities, outfile)
            if answer == "u":
                u_entities[e] = all_entities[e]
                with open('data/u_entities.json', 'w') as outfile:
                    json.dump(u_entities, outfile)
        except UnicodeEncodeError:
            print("-")

