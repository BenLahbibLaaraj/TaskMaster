def print_tasks(list_setting, tasks):
	print("\n\n(events are shown earliest first)")
	
	if list_setting == 1:
		print("Tasks:\n")
	if list_setting == 2:
		print("Recurring tasks:\n")

	for task in tasks:
		print(task)
	print("\n")