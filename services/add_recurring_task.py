from models.recurring_task import RecurringTask

def add_recurring_task(connection):
	title = ""
	while title == "":
		title = input("Give your recurring task a title: ")
	description = input("\n\n(leave blank for no description)\nGive your recurring task a description: ")
	deadline = input("\n\n(leave blank for no deadline and no frequency)\nGive your recurring task a deadline: ")
	if deadline != "":
		frequency = input("\n\n(leave blank for no frequency)\nGive your recurring task a frequency: ")
	else:
		frequency = ""

	added_recurring_task = RecurringTask(title, description, deadline, frequency)

	cursor = connection.cursor()
	cursor.execute("INSERT INTO recurring_tasks(title, description, deadline, frequency) VALUES(?, ?, ?, ?)", (added_recurring_task.title, added_recurring_task.description, added_recurring_task.deadline, added_recurring_task.frequency))
	connection.commit()