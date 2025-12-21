from services.manage_tasks.list_tasks import list_tasks

def csv_xlsx():
	return input("\nChoose file type:\n1 CSV\n2 Excel\n\n")

def export_tasks(connection):
	file_type = csv_xlsx()
	task_type = list_tasks(connection)
	print(task_type)