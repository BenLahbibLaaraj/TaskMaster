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

	cols_lower = [c.lower() for c in column_names]
	deadline_idx = cols_lower.index("deadline") if "deadline" in cols_lower else None

	for task in tasks:
		row = []
		for i, value in enumerate(task):
			text = "" if value is None else str(value)
			
			if deadline_idx is not None and i == deadline_idx and text:
				for fmt in (
					"%Y-%m-%d",
					"%Y-%m-%d %H:%M:%S",
					"%d-%m-%Y"
				):
					try:
						date_val = datetime.datetime.strptime(text, fmt).date()
						break
					except ValueError:
						date_val = None
				if date_val:
					today = datetime.date.today()
					if date_val > today:
						text = f"{GREEN}{text}{RESET}"
					elif date_val == today:
						text = f"{YELLOW}{text}{RESET}"
					else:
						text = f"{RED}{text}{RESET}"
			row.append(text)
		print("\t".join(row))