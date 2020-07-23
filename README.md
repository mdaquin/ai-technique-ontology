Initial work on creating an ontology of AI techniques.

Currently, extracts hierarchy of entities below the "AI" entity in wikidata by querying the sparql endpoint of wikidata (or a local version of it, as the one of wikidata has strong limitations wrt. number of requests that can be sent).

- copy config.py.template into config.py
- change the eid if another entity than Artificial Intelligence is to be extracted
- change the endpoint if using a local version

requires SPARQLWrapper.

Note that the script will carry on possibly forever as the hierarchy of wikidata is far from clean. I don't believe it is cycle-free and it will branch to completely irrelevant concepts. The script is therefore interuptable. data/entities will include all the results up to a point, and since it is a breadth first exploration of the tree, it should include results up to a certain level. In the case of Artificial intelligence, it crashes with a MemoryError after a while if not listing some large irrelevant entities in the "toexclude" list, but everything collected up to that point is kept.

the list_labels script list the entities and their labels, if present, to check what is included.

The manual_filer script takes random entities and ask for their relevance.



