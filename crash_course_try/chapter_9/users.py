class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self, **info):
        print(f"name of the user:{self.first_name} {self.last_name}")
        print(f'other information about {self.first_name}')
        for k, v in info.items():
            if k == 'age':
                print(f"he is {v}")
            else:
                print(f"{k} in {v}")

    def greeting(self):
        print(f"hello {self.first_name} {self.last_name}")


u = User('dawit', 'yitagesu')
u.greeting()
u.describe_user(highschool='hawassa', university='debrebrhan', age=21)
