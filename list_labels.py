import json

data = {}

with open("data/entities.json") as f:
    data = json.load(f)

for i in data:
    if "label" in data[i]:
        try: 
            print(i+" -\t"+data[i]["label"].decode("utf8"))
        except UnicodeEncodeError:
            print(i)
    else:
        print(i)        
