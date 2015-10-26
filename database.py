class DatabaseError(Exception):
	pass

class Database():
	def __init__(self, name):
		self.name = name
		self.db = {}
		self.lastfname = None
	def load(self, dbset):
		if not isinstance(dbset, dict):
			raise TypeError("dbset should be a dictionary")
			return
		self.db = dbset
	def load_file(self, path_to_dbset):
		if not isinstance(path_to_dbset, str):
			raise TypeError("path_to_dbset should be a string")
			return
		f = open(path_to_dbset)
		exec "self.db = %s" % f.read()
		f.close()
	def createTable(self, tablename):
		self.db[tablename] = {"columns": {}, "rows": {}}
	def createColumn(self, table, columnid, columnname, columntype):
		self.db[table]['columns'][columnid] = (columnname, columntype)
	def createRow(self, table, rowid, values):
		if not isinstance(values, list):
			raise TypeError("values should be a list")
		nvalues = []
		for value in values:
			exec "nvalues.append(self.db[table]['columns'][%s][1](value))" % values.index(value)
		self.db[table]['rows'][rowid] = nvalues
	def deleteTable(self, tablename):
		del self.db[tablename]
	def deleteColumn(self, table, columnid):
		del self.db[table]['columns'][columnid]
	def deleteRow(self, table, rowid):
		del self.db[table]['rows'][rowid]
	def save(self, filename=None):
		if filename==None:
			fname = self.lastfname
		else:
			fname = filename
		f = open(fname, "w")
		f.write(str(self.db))
		f.close()
		self.lastfname = fname
	def donothing(self, *args, **kwargs):
		pass
