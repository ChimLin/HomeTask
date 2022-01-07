# 1) Создайте класс сотрдник. Свойства класса - имя, оклад
# 2) Вывести в отдельном методе всех сотрудников с окладом от 30000
# 3) Сделать метод для нахождения сотрудника с максимальным окладом.
#     Метод должен вернуть объект из которого мы выведем имя сотрудника

# class Man:
#     # fio = "Иван"
#     def __init__(self,name,year):
#         self.name = name
#         self.year = year
#         self.profession = 'Программист'
#
#     # def set(self,name,year):
#     #     self.name = name
#     #     self.year = year
#     #     self.profession = 'Программист'
#
#     def get_age(self):
#         return 2021 - self.year
#     def show_info(self):
#         print(f"Добрый день, {self.name}. Ваш возраст: {self.get_age()}, профессия: {self.profession}")
#
#
#
# class Employee:
#
#     def __init__(self, name, wage):
#         self.name = name
#         self.wage = wage
#
#
# def get_wage(self):
#     return self.wage
#
#
# def employee_to_string(self):
#     print(f" имя работника {self.name}, его оклад {eself.wag}")
#
#
# def print_employees(self, employees):
#     for employee in employees:
#         if employee.get_wage() >= 30000:
#             print(employee.to_string())
#
#
# def max_wage(self, employees):
#     wage = employees[0]
#     for x in employees:
#         if x.get_wage() > wage.get_wage():
#             wage = x
#     return wage

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def findEmployeeSalaryMore30000List(listEmployee):
        employeeMore30000 = []
        for i in listEmployee:
            if i.salary >= 25000:
                employeeMore30000.append(i)
        return employeeMore30000

    def findMaxSalary(listEmployee):
        maxSalary = listEmployee[0]

        for i in listEmployee:
            if maxSalary.slary < i.salary:
                maxSalary = i

        return maxSalary


# from Employee import *
#
#
# man1 = Employee("Иван", 20000)
# man2 = Employee("Петр", 30000)
# man3 = Employee("Алексей", 25000)
#
# men = [man1, man2, man3]
#
# a = Employee.findEmployeeSalaryMore30000List(men)
# print(a)
# b = Employee.findMaxSalary(men)
# print(b)
#
