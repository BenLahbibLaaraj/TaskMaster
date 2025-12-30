from config.db_config import db_setup, close_connection

from services.manage_tasks.list_tasks import list_tasks
from services.add_tasks.choose_add import choose_add
from services.manage_tasks.export_tasks import export_tasks

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
		print("\n1 Overview (recurring) tasks")
		print("2 Add (recurring) task")
		print("3 Export (recurring) tasks")
		print("4 Exit TaskMaster")

		option = int(input("\nChoose an option: "))

		match option:
			case 1:
				list_tasks(connection)
			case 2:
				choose_add(connection)
			case 3:
				export_tasks(connection)
			case 4:
				close_connection(connection)
				menu_loop = False

if __name__ == "__main__":
    main_menu()