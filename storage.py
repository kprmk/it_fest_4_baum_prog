import sqlite3

class Storage:
	def __init__(self):
		self.cnct = sqlite3.connect('data.db')
		self.crs = self.cnct.cursor()
		self.create_table()

	def create_table(self):
		self.crs = self.cnct.execute('''CREATE TABLE IF NOT EXISTS score_table (
											name text, score int		)''')

	def insert_into(self, name_usr, score):
		self.crs.execute(f'''INSERT INTO score_table (name, score) 
								VALUES('{name_usr}', '{score}')''')
		self.cnct.commit()

	def select_all(self):
		self.crs.execute('''SELECT * FROM score_table ''')
		return self.crs.fetchall()

	def __del__(self):
		self.cnct.close()
