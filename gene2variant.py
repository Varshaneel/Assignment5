#!/usr/bin/env python
import requests, sys
import fileinput 
import json
import re
import urllib, json

Lookup_genename={}

gene = raw_input("Please type your gene name, all caps, and press enter ")
#The input is the HUGO gene name provided by the user
for line in fileinput.input(['/home/varsha/Python/Homo_sapiens.GRCh37.75.gtf']):
    gene_id_matches = re.findall('gene_id \"(.*?)\";',line)
    gene_name_matches = re.findall('gene_name \"(.*?)\";',line)
    if gene_id_matches:
       if gene_name_matches:
          Lookup_genename[gene_name_matches[0]] = gene_id_matches[0]            
print "The variants in the gene " , gene , Lookup_genename[gene] , "are:"

url = "http://rest.ensembl.org/overlap/id/" + Lookup_genename[gene] + ".json?feature=variation"
weburl = urllib.urlopen(url)
data = json.loads(weburl.read())
#print(data)
#for i in data:
   # print "Variant" + "\t" +  i["id"] + "\t" +  "is a" + "\t" + i["consequence_type"]
 #   if (i[0]["clinical_significance"] != []):

for i in range(0,len(data)):
    dic = data[i]
    geneid = dic["id"]
    cons_type = dic["consequence_type"]
    clin_sig = dic["clinical_significance"]
    if clin_sig:
       print "Variant" + "\t" + geneid  + "\t" +  "is a" + "\t" + cons_type + "\t"+  "and is clinically" + "\t" +  clin_sig[0].upper() 
    else:
       print "Variant" + "\t" + geneid  + "\t" +  "is a" + "\t" + cons_type
