def list_tasks(connection):
	list_setting = int(input("\nChoose your view:\n1 Only list tasks\n2 Only list recurring tasks\n3 List tasks and recurring tasks\n\n"))

	cursor = connection.cursor()

	t1 = "tasks"
	t2 = "recurring_tasks"

	statement = "SELECT * FROM "
	if list_setting == 1:
		cursor.execute(statement + t1)
		print("\n\nTasks:\n", cursor.fetchall(), "\n")
	elif list_setting == 2:
		cursor.execute(statement + t2)
		print("\n\nRecurring tasks:\n", cursor.fetchall(), "\n")
	else:
		cursor.execute(statement + t1)
		t_result = cursor.fetchall()
		cursor.execute(statement + t2)
		rt_result = cursor.fetchall()
		print(f"\n\nTasks:\n{t_result}\n\nRecurring tasks:\n{rt_result}\n")