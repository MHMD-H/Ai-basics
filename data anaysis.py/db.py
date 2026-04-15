import sqlite3
conn = sqlite3.connect("database name","user","password") #connect to data base

#quiers 
cur = conn.cursor()#جلب الاستعلامات والنتائج

cur.execute("select * From user")#(select (columns name) from (table name) (where/limit) (condition);)
cur.fetchall()#retrieve data as tuple
conn.commit()#to save changes 
conn.close()

