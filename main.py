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

task1 = Task("meeting")
print(task1.title)

recurring_task1 = RecurringTask("meeting", "daily", "quarterly report")
print(recurring_task1.title, recurring_task1.description, recurring_task1.frequency)