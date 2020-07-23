import json
import sys

data = {}

with open(sys.argv[1]) as f:
    data = json.load(f)

for i in data:
    if "label" in data[i]:
        try: 
            print(i+" -\t"+data[i]["label"].decode("utf8"))
        except UnicodeEncodeError:
            print(i)
    else:
        print(i)        
