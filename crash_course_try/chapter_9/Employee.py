class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f"{self.first} {self.last}"


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('--->>', emp.fullname())


emp_1 = Employee('nahom', 'dejene', 9000)
emp_2 = Employee('dawit', 'yitagesu', 50_000)
print(emp_1.fullname())
print(emp_1.email)
print(Employee.fullname(emp_2))
print(emp_2.email)
print()
####################################
dev_1 = Developer('devid', 'majur', 900000, 'python')
print(dev_1.fullname())
print(dev_1.prog_lang)
print()
##################################

mgr_1 = Manager('devo', '.tiller', 100_0000, [emp_1, dev_1])
print(mgr_1.email)
mgr_1.print_emp()
mgr_1.remove(emp_1)
mgr_1.print_emp()
