from config.db_config import db_setup, close_connection

from services.manage_tasks.list_tasks import list_tasks
from services.add_tasks.add_task import add_task
from services.add_tasks.add_recurring_task import add_recurring_task
from services.manage_tasks.export_tasks import csv_xlsx

print("""
##########################################################################
#                                                                        #
#  TTTTT   AAA   SSSSS  K   K  M   M   AAA   SSSSS  TTTTT  EEEEE  RRRRR  #
#    T    A   A  S      K  K   MM MM  A   A  S        T    E      R   R  #
#    T    AAAAA  SSSSS  KKK    M M M  AAAAA  SSSSS    T    EEEE   RRRR   #
#    T    A   A      S  K  K   M   M  A   A      S    T    E      R  R   #
#    T    A   A  SSSSS  K   K  M   M  A   A  SSSSS    T    EEEEE  R   R  #
#                                                                        #
#                  Master your day, one task at a time.                  #
#                                                          	             #
##########################################################################
""")

def main_menu():
	connection = db_setup()

	menu_loop = True
	while menu_loop == True:
		print("1 Overview (recurring) tasks")
		print("2 Add task")
		print("3 Add recurring task")
		print("4 Export (recurring) tasks")
		print("5 Exit TaskMaster")

		option = int(input("\nChoose an option: "))

		match option:
			case 1:
				list_tasks(connection)
			case 2:
				add_task(connection)
			case 3:
				add_recurring_task(connection)
			case 4:
				export_tasks()
			case 5:
				close_connection(connection)
				menu_loop = False

if __name__ == "__main__":
    main_menu()