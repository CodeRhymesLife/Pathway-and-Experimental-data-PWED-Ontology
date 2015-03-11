'''
Created on 2015. 3. 9.

@author: Ryan James
'''
from urllib.request import Request, urlopen, URLError
from xml.dom import minidom
import json

pmid_list = ["http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21057493"]

class Entity:
	json = {};
	
	def __init__ (self, json):
		self.json = json;

class Publication(Entity):
	All = {};
	
	def __init__ (self, json):
		super(Publication, self).__init__(json);
		Publication.All[self.json['accession']] = self;
		
	def toString (self):
		authorsString = "";
		for author in self.json['authors'].split(','):
			authorsString += "\t:author \"" + author.strip() + "\"^^xsd:string ;\n";
		
		return	(self.getId() + " rdf:type :Publication , :NamedIndividual ;\n"
				"" + authorsString + ""
				"\t:title \"" + self.json['title'] + "\"^^xsd:string .");
				
	def getId (self):
		return ":pub_" + str(self.json['accession']);
		
class Experiment(Entity):
	Species = {"Homo sapiens": ":homo_sapien"};

	def toString (self):
		publication = Publication(self.json['bibliography'])
	
		return (":exp_" + self.json['accession'] + " rdf:type :Experiment , :NamedIndividual ;\n"
				"\t:species " + Experiment.Species[self.json['species']] + " ;\n"
				"\t:name \"" + self.json['name'] + "\"^^xsd:string ;\n"
				"\t:year \"" + self.json['releasedate'] + "\"^^xsd:string ;\n"
				"\t:publication " + publication.getId() + " ;\n"
				"\t:description \"" + self.json['description']['text'] + "\"^^xsd:string .");
				
	
experiments = [];
for query in pmid_list:
    pmid = query[-8:]
    pmid_req = Request(query)
    pmid_res = urlopen(pmid_req)
    queryResultJson = json.loads(pmid_res.read().decode('utf8'))
    experiments.append(Experiment(queryResultJson['experiments']['experiment']));
	
print ("Experiments:\n\n")
for exp in experiments:
	print (exp.toString() + "\n\n")

print ("\n\n\n\nPublications:\n\n")	
for id, pub in Publication.All.items():
	print (pub.toString() + "\n\n")