def print_tasks(list_setting, tasks):
	print("\n\n(events are shown earliest first)")

	if list_setting == 1:
		print("Tasks:\n")

		for task in tasks:
			print(f"{task[0]}\t{task[1]}\t{task[2]}")
		print("\n")
		
	if list_setting == 2:
		print("Recurring tasks:\n")

		for task in tasks:
			print(f"{task[0]}\t{task[1]}\t{task[2]}\t{task[3]}")
		print("\n")