import os
import csv
import pandas as pd

from services.manage_tasks.list_tasks import list_tasks

def destination_folder():
	return input("\n(leave empty for default folder 'TaskMaster/exports/')\nChoose destination folder: ")

def file_title():
	return input("\nType filename (without file extension): ")

def file_type():
	return int(input("\nChoose file type:\n1 CSV\n2 Excel\n\n"))

def check_if_recurring(tasks):
	if len(tasks[0]) == 3:
		return False
	else:
		return True

def export_csv(filename, tasks):
	with open(filename, mode="w", newline="", encoding="utf8") as file:
		writer = csv.writer(file)
		if check_if_recurring(tasks):
			writer.writerow(["title", "description", "deadline", "frequency"])
		else:
			writer.writerow(["title", "description", "deadline"])
		writer.writerow([])
		for task in tasks:
			writer.writerow(task)

def export_xlsx(filename, tasks):
	if check_if_recurring(tasks):
		df = pd.DataFrame(tasks, columns=["title", "description", "deadline", "frequency"])
	else:
		df = pd.DataFrame(tasks, columns=["title", "description", "deadline"])
	df.to_excel(filename, index=False)

def export_tasks(connection):
	default_folder = "exports/"

	prefix = default_folder + destination_folder()
	if not prefix.endswith("/"):
		prefix += "/"

	interfix = file_title()

	suffix = file_type()
	if prefix == "exports/":
		if suffix == 1:
			prefix = prefix + "csv/"
		else:
			prefix = prefix + "xlsx/"
	if not os.path.exists(prefix):
		os.makedirs(prefix)

	task_type = list_tasks(connection)
	if suffix == 1:
		filename = prefix + interfix + ".csv"
		export_csv(filename, task_type)
	else:
		filename = prefix + interfix + ".xlsx"
		export_xlsx(filename, task_type)