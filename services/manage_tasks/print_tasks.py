import datetime

def print_tasks(connection, list_setting, statement, tasks):
	cursor = connection.cursor()

	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	RED = '\033[31m'
	RESET = '\033[0m'

	print("\n\n(tasks are shown earliest first)")

	if list_setting == 1:
		print("Tasks:\n")

	if list_setting == 2:
		print("Recurring tasks:\n")

	cursor.execute(statement)
	column_names = [description[0] for description in cursor.description]
	print("\t".join(column_names))

	for task in tasks:
		print("\t".join(str(value) for value in task))