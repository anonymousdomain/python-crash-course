cars=['lamborgini','bmw','audi','ford']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
#var.lower()>> ignor case
cars.append('Ferari')
print(cars)
for car in cars:
    if car.lower()=='ferari':
        print(car.capitalize())
    else:
        print(car)