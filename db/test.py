import sqlite3
import os 

os.remove('serverdata.db')

conn = sqlite3.connect("serverdata.db")

gcur = conn.cursor()

gcur.execute("CREATE TABLE ServerData(ID INTEGER PRIMARY KEY, CAPTCHA INTEGER, AUTOMOD INTEGER, ANTISPAM INTEGER, LEVELSYS INTEGER, SETUP INTEGER)")

conn.commit()

conn.close()
