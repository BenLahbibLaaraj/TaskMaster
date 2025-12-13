from models.task import Task

class RecurringTask(Task):
	def __init__(self, title, description, deadline, frequency):
		super().__init__(title, description, deadline)
		self.frequency = frequency if frequency != "" else None