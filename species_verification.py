'''
Created on 2015. 3. 3.

@author: daehyun
'''
from urllib2 import Request, urlopen, URLError
from xml.dom import minidom
import json
from matplotlib._cntr import Cntr

pmid_list = ["http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21057493",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=23812591",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21295276",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21451524",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=22466170",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=20075857",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=20123894",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21170310",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=19571010",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=18974828",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21602795",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21551231",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=20805998",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=17540599",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21551231",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21602795",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=20805998",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=20090754",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21875955",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=17540599",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21602795",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21551231",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=20805998",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=17114293",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=17114293",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21602795",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21551231",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=20805998",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21602795",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21551231",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=20805998",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=17114293",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=19829295",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=21630377",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=20953172",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=14688391",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=20837710",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=17183653",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=19128516",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=20508642",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=16713582",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=19187765",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=19187766",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=22144582",
"http://www.ebi.ac.uk/arrayexpress/json/v2/experiments?pmid=22421046"]

cnt_expdata = 0;
cnt_exp = 0;

array_set = set()

accession_dict = dict()

for query in pmid_list:
    pmid = query[-8:]
    pmid_req = Request(query)
    pmid_res = urlopen(pmid_req)
    pmid_txt = json.loads(pmid_res.read())
    cur_exp = pmid_txt['experiments']['experiment']
    print ":pmid_"+pmid+" rdf:type :Publication, :NamedIndividual; :hasid \""+pmid+"\"^^xsd:string."
    #print query;
    if type(cur_exp) ==list:
        cnt = 0;
        for i in cur_exp:
            cnt_expdata = cnt_expdata+1
            print ":expementset"+str(cnt_expdata)+" rdf:type :ExperimentSet, :NamedIndividual; :haspmid :pmid_"+pmid
            if (type(i['species']) == list):
                for j in i['species']:
                    print "; :hasorganism \""+j+"\"^^xsd:string"
            else:
                print "; :hasorganism \""+i['species']+"\"^^xsd:string" 
            if i.has_key('secondaryaccession'):
                if type(i['secondaryaccession']) != list:
                    print "; :hasid \""+i['secondaryaccession']+"\"^^xsd:string "
                else:
                    for j in i['secondaryaccession']:
                        print "; :hasid \""+j+"\"^^xsd:string "
            else:
                print "; :hasid \""+i['accession']+"\"^^xsd:string "
            if(type(i['experimenttype']) == list):
                for j in i['experimenttype']:
                    print "; :hasexperimenttype \""+j+"\"^^xsd:string"
            else:
                print "; :hasexperimenttype \""+i['experimenttype']+"\"^^xsd:string"
            if i.has_key('arraydesign'):
                if type(i['arraydesign']) == list:
                    for j in i['arraydesign']:
                        print "; :hasarraydesign \""+j['name']+"\"^^xsd:string"
                        array_set.add(j['name'])
                else:
                    print "; :hasarraydesign \""+i['arraydesign']['name']+"\"^^xsd:string"
                    array_set.add(i['arraydesign']['name'])
            #print "protocols"
            if type(i['protocol']) == list:
                for j in i['protocol']:
                    po = 0
                    if not accession_dict.has_key(j['accession']):
                        cnt_exp  = cnt_exp+1
                        accession_dict[j['accession']] = cnt_exp
                    po = accession_dict[j['accession']]
                        
                    print "; :hasexperimentdata :Experiment"+str(po)
            else:
                po = 0
                if not accession_dict.has_key(j['accession']):
                    cnt_exp  = cnt_exp+1
                    accession_dict[j['accession']] = cnt_exp
                po = accession_dict[j['accession']]
                
                print "; :hasexperimentdata :Experiment"+str(po)
            print "."
    else:
        cnt_expdata = cnt_expdata+1
        print ":expementset"+str(cnt_expdata)+" rdf:type :ExperimentSet, :NamedIndividual; :haspmid :pmid_"+pmid
        if (type(cur_exp['species']) == list):
            for j in cur_exp['species']:
                print "; :hasorganism \""+j+"\"^^xsd:string"
        else:
            print "; :hasorganism \""+cur_exp['species']+"\"^^xsd:string"       
        if cur_exp.has_key('secondaryaccession'):
            if type(cur_exp['secondaryaccession']) != list:
                #print cur_exp['secondaryaccession']
                print "; :hasid \""+cur_exp['secondaryaccession']+"\"^^xsd:string "
            else:
                for j in cur_exp['secondaryaccession']:
                    #print j
                    print "; :hasid \""+j+"\"^^xsd:string "
        else:
            print "; :hasid \""+cur_exp['accession']+"\"^^xsd:string "
            #print cur_exp['accession']
        #print cur_exp['experimenttype']
        if(type(cur_exp['experimenttype']) == list):
            for j in cur_exp['experimenttype']:
                print "; :hasexperimenttype \""+j+"\"^^xsd:string"
        else:
            print "; :hasexperimenttype \""+cur_exp['experimenttype']+"\"^^xsd:string"
        
        if cur_exp.has_key('arraydesign'):
            if type(cur_exp['arraydesign']) == list:
                for j in cur_exp['arraydesign']:
                    print "; :hasarraydesign \""+j['name']+"\"^^xsd:string"
                    array_set.add(j['name'])
            else:
                print "; :hasarraydesign \""+cur_exp['arraydesign']['name']+"\"^^xsd:string"
                array_set.add(cur_exp['arraydesign']['name'])
        if type(cur_exp['protocol']) == list:
            for j in cur_exp['protocol']:
                if j.has_key('accession'):
                    po = 0
                    if not accession_dict.has_key(j['accession']):
                        cnt_exp  = cnt_exp+1
                        accession_dict[j['accession']] = cnt_exp
                    po = accession_dict[j['accession']]
                    print "; :hasexperimentdata :Experiment"+str(po)
        else:
            if not accession_dict.has_key(cur_exp['protocol']['accession']):
                cnt_exp  = cnt_exp+1
                accession_dict[cur_exp['protocol']['accession']] = cnt_exp
            po = accession_dict[cur_exp['protocol']['accession']]
            print "; :hasexperimentdata :Experiment"+str(po)
        print "."
    
for keys in accession_dict.keys():
    print ":Experiment"+str(accession_dict[keys])+" rdf:type :Experiment, :NamedIndividual; :hasid \""+keys+"\"^^xsd:string."
    
print array_set
'''    p = xmldoc
    p.findall('species')
    for i in p:
        print i.toxml();

    exit()'''