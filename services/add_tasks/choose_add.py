from services.add_tasks.add_task import add_task
from services.add_tasks.add_recurring_task import add_recurring_task

def choose_add(connection):
	choice = int(input("\nChoose the type of task you want to add:\n1 Task\n2 Recurring task\n\n"))

	if choice == 1:
		add_task(connection)
	else:
		add_recurring_task(connection)