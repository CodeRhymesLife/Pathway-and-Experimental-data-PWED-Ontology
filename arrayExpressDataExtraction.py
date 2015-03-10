'''
Created on 2015. 3. 9.

@author: Ryan James
'''
from urllib.request import Request, urlopen, URLError
from xml.dom import minidom
import json

pmid_list = ["http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21057493"]

class Publication:
	pubmedId = 0;
	title = "";
	authors = [];
	
	def __init__ (self, json):
		self.pubmedId = json['accession'];
		self.title = json['title'];
		self.authors = json['authors'].split(',');
		
	def toString (self):
		return "id: " + str(self.pubmedId) + ", title: " + self.title + ", authors: " + ", ".join(self.authors); 

for query in pmid_list:
    pmid = query[-8:]
    pmid_req = Request(query)
    pmid_res = urlopen(pmid_req)
    queryResultJson = json.loads(pmid_res.read().decode('utf8'))
    exp = queryResultJson['experiments']['experiment']
    print (":pmid_"+pmid+" rdf:type :Publication, :NamedIndividual; :hasid \""+pmid+"\"^^xsd:string.")
    species = exp['species'];
    id = exp['miamescores'];
    name = exp['name'];
    year = exp['releasedate'];
    description = exp['description']['text'];
    publication = Publication(exp['bibliography']);
    print("Publication -> " + publication.toString());
	
	# prase relevant data
	# encode in ontology