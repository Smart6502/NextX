import sqlite3

conn = sqlite3.connect("levelstate.db")

gcur = conn.cursor()

gcur.execute("CREATE TABLE(ID INTEGER, State TEXT, Changes INTEGER)")

conn.commit()
