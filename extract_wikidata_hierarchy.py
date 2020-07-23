from SPARQLWrapper import SPARQLWrapper, JSON
import time
import json
import config
import sys

# ids of entities to complete
tocomplete = [config.eid]

# ids already done
completed = []

# sparql endpoint of wikidata
sparql = SPARQLWrapper(config.endpoint)

# the final results as a dicionary of id and relations
entities = {}

def query(q, v):
    sparql.setQuery(q)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    list = []
    for c in results['results']['bindings']:
        list.append(c[v]['value'])
    return list


def process(id, l, a):
    entities[id][a] = []
    for r in l:
        if 'http' in r:
            r = r[31:]
        entities[id][a].append(r)
        if not r in tocomplete and not r in completed and not r in config.toexclude:
            tocomplete.append(r)

def complete(id):
    before = len(tocomplete)
    print("completing https://www.wikidata.org/wiki/"+id+" ("+str(len(completed))+"/"+str(len(tocomplete))+")")
    entities[id] = {}
    # subclassof P279
    results = query('SELECT ?item WHERE {?item wdt:P279 wd:'+id+'}', 'item')
    process(id, results, "subclasses")
    # partOf P361
    results = query('SELECT ?item WHERE {?item wdt:P361 wd:'+id+'}', 'item')
    process(id, results, "parts")    
    # instanceOf P31
    results = query('SELECT ?item WHERE {?item wdt:P31 wd:'+id+'}', 'item')
    process(id, results, "instances")
    # label
    results = query('SELECT ?label where {wd:'+id+' rdfs:label ?label . filter (lang(?label) = "en")}',
                    "label")
    if len(results) > 0:
        entities[id]["label"] = results[0]
    if len(tocomplete)-before > config.interuptifmore:
        print("XXX https://www.wikidata.org/wiki/"+id+" generated a lot of stuff")
        if "label" in entities[id]:
            try:
                print(entities[id]["label"])
            except UnicodeEncodeError:
                print ("-")
        if len(completed)>config.interuptafter:
            sys.exit()
    
while(len(tocomplete)!=0):
    id = tocomplete.pop(0)
    complete(id)    
    with open('data/entities.json', 'w') as outfile:
        json.dump(entities, outfile)
    completed.append(id)
    # stop if too many requests
    # time.sleep(1)
print(entities)
