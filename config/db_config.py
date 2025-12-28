import os, sqlite3

DB_PATH = os.getenv("DB_PATH", "db/taskmaster.db")

def db_setup():
	if os.path.isfile(DB_PATH) == False:
		connection = sqlite3.connect(DB_PATH)
		cursor = connection.cursor()
		cursor.executescript("""
				CREATE TABLE tasks(
		    	title TEXT NOT NULL,
		    	description TEXT,
		    	deadline DATE);

				CREATE TABLE recurring_tasks(
		    	title TEXT NOT NULL,
		    	description TEXT,
		    	deadline DATE,
		    	frequency TEXT);
		    	""")
	else:
		connection = sqlite3.connect(DB_PATH)


	return connection

def close_connection(connection):
	print("\nExited application.")
	connection.cursor().close()
	connection.close()
	print("Database conection closed securely.\n")