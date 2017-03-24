import simplejson
import facebook
import hashlib
import sys
import sqlite3 as lite
import contextlib
from datetime import datetime
import pdb

conn = lite.connect('./fb.sqlite')
# conn.text_factory = str
cur = conn.cursor()
data = cur.execute("SELECT * FROM People")

f = open('output.csv', 'w')
print >> f, "person_hash_id, person_id, person_name"
for row in data:
  print >> f, row
f.close()