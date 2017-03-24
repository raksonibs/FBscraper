# -*- coding: utf-8 -*- 
import simplejson
import facebook
import hashlib
import sys
import sqlite3 as lite
import contextlib
from datetime import datetime
import pdb
import csv

conn = lite.connect('./fb.sqlite')
conn.text_factory = str
cur = conn.cursor()
data = cur.execute("SELECT * FROM People")

# open('output.csv', 'w')
fout = open('output.csv','w')
# writer = csv.writer(fout)
print >> fout, "person_hash_id, person_id, person_name"
# writer.writerows(["person_hash_id", "person_id", "person_name"])

for row in data:
  hash_value = row[0]
  person_id = row[1]
  person_name = row[2]

  row = "{0}, {1}, {2}".format(hash_value, person_id, person_name)
  print >> fout, row
  # writer.writerows([hash_value, person_id, person_id])
fout.close()