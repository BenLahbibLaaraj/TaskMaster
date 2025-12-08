from models.task import Task

def add_task(connection):
	title = input("Give your task a title: ")
	description = input("\n(leave blank for no description)\nGive your task a description: ")
	deadline = input("\n(leave blank for no deadline)\nGive your task a deadline: ")

	added_task = Task(title, description, deadline)

	cursor = connection.cursor()
	cursor.execute("INSERT INTO tasks(title, description, deadline) VALUES(?, ?, ?)", (added_task.title, added_task.description, added_task.deadline))
	connection.commit()