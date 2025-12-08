import os, sqlite3

DB_PATH = os.getenv("DB_PATH", "db/taskmaster.db")

def db_setup():
	connection = sqlite3.connect(DB_PATH)
	if os.path.isfile(DB_PATH) == False:
		cursor = connection.cursor()
		cursor.executescript("""
				CREATE TABLE tasks(
		    	title TEXT NOT NULL,
		    	description TEXT,
		    	deadline TEXT);

				CREATE TABLE recurring_tasks(
		    	title TEXT NOT NULL,
		    	description TEXT,
		    	deadline TEXT,
		    	frequency TEXT NOT NULL);
		    	""")

	return connection

def close_connection():
	print("Exited application.")
	cursor = connection.cursor()
	cursor.close()
	connection.close()
	print("Database conection closed securely.")