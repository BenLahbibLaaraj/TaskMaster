from services.manage_tasks.print_tasks import print_tasks
from services.manage_tasks.print_tasks import print_all_tasks

def list_tasks(connection):
	list_setting = int(input("\nChoose your view:\n1 Only list tasks\n2 Only list recurring tasks\n3 List tasks and recurring tasks\n\n"))

	cursor = connection.cursor()

	t1 = "tasks"
	t2 = "recurring_tasks"

	statement = "SELECT * FROM "
	if list_setting == 1:
		cursor.execute(statement + t1)
		results = cursor.fetchall()
		print_tasks(list_setting, results)
		return results
	elif list_setting == 2:
		cursor.execute(statement + t2)
		results = cursor.fetchall()
		print_tasks(list_setting, results)
		return results
	else:
		cursor.execute(statement + t1)
		t_results = cursor.fetchall()
		cursor.execute(statement + t2)
		rt_results = cursor.fetchall()
		print_all_tasks(t_results, rt_results)
		return False