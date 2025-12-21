from models.recurring_task import RecurringTask
from services.add_tasks.validate_deadline import is_deadline_valid

def add_recurring_task(connection):
	title = ""
	while title == "":
		title = input("Give your recurring task a title: ")
	description = input("\n\n(leave blank for no description)\nGive your recurring task a description: ")
	while True:
		deadline = input("\n\n(leave blank for no deadline)\nGive your task a deadline DD-MM-YYYY: ")
		if is_deadline_valid(deadline):
			break
	if deadline != "":
		frequency = input("\n\n(leave blank for no frequency)\nGive your recurring task a frequency: ")
	else:
		frequency = ""

	added_recurring_task = RecurringTask(title, description, deadline, frequency)

	cursor = connection.cursor()
	cursor.execute("INSERT INTO recurring_tasks(title, description, deadline, frequency) VALUES(?, ?, ?, ?)", (added_recurring_task.title, added_recurring_task.description, added_recurring_task.deadline, added_recurring_task.frequency))
	connection.commit()