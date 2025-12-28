from services.manage_tasks.print_tasks import print_tasks

def list_tasks(connection):
	list_setting = int(input("\nChoose your view:\n1 Only list tasks\n2 Only list recurring tasks\n3 List tasks and recurring tasks\n\n"))

	cursor = connection.cursor()

	statement_t = "SELECT * FROM tasks"
	statement_rt = "SELECT * FROM recurring_tasks"
	filter_date = " ORDER BY deadline DESC"

	if list_setting == 1:
		cursor.execute(statement_t + filter_date)
		results = cursor.fetchall()
		print_tasks(list_setting, results)
		return results
	elif list_setting == 2:
		cursor.execute(statement_rt + filter_date)
		results = cursor.fetchall()
		print_tasks(list_setting, results)
		return results
	else:
		cursor.execute(statement_t + filter_date)
		results = cursor.fetchall()
		print_tasks(1, results)

		cursor.execute(statement_rt + filter_date)
		results = cursor.fetchall()
		print_tasks(2, results)

		return False