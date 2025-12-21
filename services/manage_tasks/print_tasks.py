def print_tasks(list_setting, tasks):
	if list_setting == 1:
		print("\n\nTasks:\n")
	elif list_setting == 2:
		print("\n\nRecurring tasks:\n")

	for task in tasks:
		print(task)
	print("\n")

def print_all_tasks(tasks, recurring_tasks):
	print("\n\nTasks:\n")
	for task in tasks:
		print(task)
	print("\nRecurring tasks:\n")
	for recurring_task in recurring_tasks:
		print(recurring_task)
	print("\n")