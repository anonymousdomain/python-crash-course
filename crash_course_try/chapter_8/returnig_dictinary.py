age = 0


def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


worker1 = build_person('dawit', 'tokler', 21)

for k, v in worker1.items():
    print(f"{k} name is {v}")

worker2 = build_person('samuel', 'seralign')
for k, v in worker2.items():
    print(f"{k} name is {v}")
