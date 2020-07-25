import attributes
import sys
import json

if len(sys.argv) != 2:
    print("please provide a file name")
    sys.exit()

str=","
count = 0
for a in attributes.a:
    for v in attributes.a[a]:
        str+=","+a+"::"+v
        count=count+1
        
str+="\n"

data = {}

with open(sys.argv[1]) as f:
    data = json.load(f)

for i in data:
    str+=i+","+data[i]["label"]
    for j in range(0, count):
        str+=","
    str+="\n"

print(str)

