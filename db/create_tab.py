import sqlite3

conn = sqlite3.connect("mainbank.db")

gcur = conn.cursor()

gcur.execute("CREATE TABLE Balance(ID INTEGER PRIMARY KEY, JOB TEXT, BALANCE INTEGER)")

conn.commit()

conn.close()