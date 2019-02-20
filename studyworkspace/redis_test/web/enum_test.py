from enum import *


weekEnum = Enum('WeekEnd', ('Mon', 'Tue', 'Wen', 'Thurs', 'Fri'))


print(weekEnum.Fri.value)
print(weekEnum.Mon.value)
print(weekEnum.Tue.value)
print(weekEnum.Wen.value)
print(weekEnum.Thurs.value)