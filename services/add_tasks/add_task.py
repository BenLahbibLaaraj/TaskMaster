from models.task import Task
from services.add_tasks.validate_deadline import is_deadline_valid

def add_task(connection):
	title = ""
	while title == "":
		title = input("Give your task a title: ")
	description = input("\n\n(leave blank for no description)\nGive your task a description: ")
	while True:
		deadline = input("\n\n(leave blank for no deadline)\nGive your task a deadline DD-MM-YYYY: ")
		if is_deadline_valid(deadline):
			break

	added_task = Task(title, description, deadline)

	cursor = connection.cursor()
	cursor.execute("INSERT INTO tasks(title, description, deadline) VALUES(?, ?, ?)", (added_task.title, added_task.description, added_task.deadline))
	connection.commit()