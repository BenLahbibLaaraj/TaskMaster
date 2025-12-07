from db_config.db_config import db_setup

from tasks.task import Task
from tasks.recurring_task import RecurringTask

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

if __name__ == "__main__":
    main_menu()