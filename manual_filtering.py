import json
import os.path
import random
import sys
import config

if len(sys.argv) != 3:
    print ("provide a filename and a sentence")
    sys.exit()

dfile = sys.argv[1]
sentence = sys.argv[2]
    
all_entities = {}
with open("data/"+dfile+".json") as f:
    all_entities = json.load(f)

y_entities = {}
if os.path.isfile("data/y_"+dfile+".json"):
    with open("data/y_"+dfile+".json") as f:
        y_entities = json.load(f)

n_entities = {}
if os.path.isfile("data/n_"+dfile+".json"):
    with open("data/n_"+dfile+".json") as f:
        n_entities = json.load(f)    

u_entities = {}
if os.path.isfile("data/u_"+dfile+".json"):
    with open("data/u_"+dfile+".json") as f:
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
            answer = raw_input("Is https://www.wikidata.org/wiki/"+e+" - "+all_entities[e]["label"]+" "+sentence+"?\n y(es) - n(o) - u(nsure) - q(uit)\n")
            if answer == "q": sys.exit()
            if answer == "y":
                y_entities[e] = all_entities[e]
                with open('data/y_'+dfile+'.json', 'w') as outfile:
                    json.dump(y_entities, outfile)
            if answer == "n":
                n_entities[e] = all_entities[e]
                with open('data/n_'+dfile+'.json', 'w') as outfile:
                    json.dump(n_entities, outfile)
            if answer == "u":
                u_entities[e] = all_entities[e]
                with open('data/u_'+dfile+'.json', 'w') as outfile:
                    json.dump(u_entities, outfile)
        except UnicodeEncodeError:
            print("-")

