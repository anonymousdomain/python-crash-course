from crash_course_try.chapter_9.car import Car
my_car = Car('marcedice', 'nano5', '2025')
display = my_car.describe_car()
print(display)
my_car.update_odometer(200)
my_car.read_odometer()

print()
my_used_car = Car('ferrari', 'frBoost9', '2019')
discribe = my_used_car.describe_car()
print(discribe)
my_used_car.update_odometer(75)
my_used_car.increment_odometer(650)
my_used_car.read_odometer()


