from crash_course_try.chapter_9.car import ElectricCar
my_tesla = ElectricCar('tesla', 'model S', '2021')

s = my_tesla.describe_car()
print(s)
my_tesla.battry.describe_battry()
my_tesla.battry.get_range()
my_tesla.battry.upgrade_battry()
my_tesla.battry.describe_battry()
my_tesla.battry.get_range()
