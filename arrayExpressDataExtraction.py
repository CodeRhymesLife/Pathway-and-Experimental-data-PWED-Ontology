'''
Created on 2015. 3. 9.

@author: Ryan James
'''
from urllib.request import Request, urlopen, URLError
from xml.dom import minidom
import json

pmid_list = ["http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21057493"]

for query in pmid_list:
    pmid = query[-8:]
    pmid_req = Request(query)
    pmid_res = urlopen(pmid_req)
    pmid_txt = json.loads(pmid_res.read().decode('utf8'))
    exp = pmid_txt['experiments']['experiment']
    print (":pmid_"+pmid+" rdf:type :Publication, :NamedIndividual; :hasid \""+pmid+"\"^^xsd:string.")
    
	# prase relevant data
	# encode in ontology