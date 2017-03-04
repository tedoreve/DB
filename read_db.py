# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 12:08:45 2017

@author: tedoreve
"""

import sqlite3 as db
conn = db.connect('Mydict.db')
cursor = conn.cursor()
conn.row_factory = db.Row
cursor.execute("select * from Words")
rows = cursor.fetchall()
rows[0] = list(rows[0])
rows[0][0]='A'
rows[0] = tuple(rows[0])
file_object = open('vocabulary.html', 'w')
file_object.write("Content-type: text.html\r\n\r\n")
file_object.write("")
file_object.write("<html><body><p>")
for row in rows:
  file_object.write("%s %s %s" % ('start',row[0],row[1]))
  file_object.write("<br />")
file_object.write("</p></body></html>")
file_object.close()

#=========================the words I like=====================================
# rabbitfish
# raffia
# ragee
# rakehell
# radices
# 上次搜到的单词是 start reactant n.反应物
#==============================================================================
