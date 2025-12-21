from datetime import datetime

def is_deadline_valid(user_input):
	if (user_input) == "":
		return True

	try:
		datetime.strptime(user_input, "%d-%m-%Y")
		return True
	except ValueError:
		return False