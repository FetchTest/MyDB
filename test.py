from db import *
from os.path import join

db = Database("Grocery List")
print "Script Database Name: "+db.name

db.createTable("groceries")

db.createColumn("groceries", 0, "name", str)
db.createColumn("groceries", 1, "quantity", int)

db.createRow("groceries", 0, ["Bananas", 4])
db.createRow("groceries", 1, ["Peanut Butter", 1])
db.createRow("groceries", 2, ["Dark Chocolate Bars", 2])

name = raw_input("Name for database %s: " % db.name)
db.save(join("/home/daniel", name))
