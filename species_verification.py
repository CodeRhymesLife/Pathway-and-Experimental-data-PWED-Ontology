'''
Created on 2015. 3. 3.

@author: daehyun
'''
from urllib2 import Request, urlopen, URLError
from xml.dom import minidom

pmid_list = ["http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21057493",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=23812591",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21295276",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21451524",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=22466170",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=20075857",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=20123894",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21170310",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=19571010",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=18974828",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21602795",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21551231",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=20805998",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=17540599",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21551231",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21602795",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=20805998",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=20090754",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21875955",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=17540599",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21602795",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21551231",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=20805998",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=17114293",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=17114293",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21602795",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21551231",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=20805998",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21602795",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21551231",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=20805998",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=17114293",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=19829295",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=21630377",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=20953172",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=14688391",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=20837710",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=17183653",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=19128516",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=20508642",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=16713582",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=19187765",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=19187766",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=22144582",
"http://www.ebi.ac.uk/arrayexpress/xml/v2/experiments?pmid=22421046"]

for query in pmid_list:
    pmid_req = Request(query)
    pmid_res = urlopen(pmid_req)
    pmid_txt = pmid_res.read()
    xmldoc = minidom.parseString(pmid_txt)
    temp = xmldoc.getElementsByTagName("species")
    print query,"-",
    for i in temp:
        print i.firstChild.data,",",
    print;
'''    p = xmldoc
    p.findall('species')
    for i in p:
        print i.toxml();

    exit()'''