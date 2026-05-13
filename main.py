# 2-misol
class Car:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

c1 = Car('BMW', 45000)

print(c1.name)
print(c1.get_price())

c1.set_price(50000)
print(c1.get_price())


# 3-misol
class Phone:
    def __init__(self, model, battery):
        self.model = model
        self.__battery = battery

    def get_battery(self):
        return self.__battery

    def set_battery(self, new_battery):
        self.__battery = new_battery


p1 = Phone("Iphone 15", 90)

battery = p1.get_battery()
print(battery)

p1.set_battery(100)
print(p1.get_battery())


# 4-misol
class Teacher:
    def __init__(self, fullname, salary):
        self.fullname = fullname
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.salary = new_salary

t1 = Teacher("Alijonov Valijon", 150000)
print(t1.fullname)
print(t1.get_salary())

t1.set_salary(700)
print(t1.get_salary())


# 5-misol
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.__ram = ram

    def get_ram(self):
        return self.__ram

    def set_ram(self, new_ram):
        self.__ram = new_ram

l1 = Laptop('HP', 8)

print(l1.brand)
print(l1.get_ram())


l1.set_ram(16)
print(l1.get_ram())


# 6-misol
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

u1 = User('admin', 12345)

print(u1.username)
print(u1.get_password())


u1.set_password(54321)
print(u1.get_password())


# 7-misol
class University:
    def __init__(self, name, student_count):
        self.name = name
        self.__student_count = student_count

    def get_students_count(self):
        return self.__student_count

    def set_students_count(self, new_student_c):
        self.__student_count = new_student_c


u1 = University('TATU', 12000)

print(u1.name)
print(u1.get_students_count())

u1.set_students_count(15000)
print(u1.get_students_count())



# 8-misol
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

a1 = Animal("Sher", 5)

print(a1.name)
print(a1.get_age())

a1.set_age(6)
print(a1.get_age())


# 9-misol
class Game:
    def __init__(self, title, level):
        self.title = title
        self.__level = level

    def get_level(self):
        return self.__level

    def set_level(self, new_level):
        self.__level = new_level

g1 = Game('Minecraft', 10)

print(g1.title)
print(g1.get_level())

g1.set_level(20)
print(g1.get_level())


# 10-misol
class Hospital:
    def __init__(self, name, rooms):
        self.name = name
        self.__rooms = rooms

    def get_rooms(self):
        return self.__rooms

    def set_rooms(self, new_rooms):
        self.__rooms = new_rooms

h1 = Hospital('Shifo', 50)

print(h1.name)
print(h1.get_rooms())

h1.set_rooms(70)
print(h1.get_rooms())


# 11-misol
class Market:
    def __init__(self, name, income):
        self.name = name
        self.__income = income

    def get_income(self):
        return self.__income

    def set_income(self, new_income):
        self.__income = new_income

m1 = Market('Korzinka', 100000)

print(m1.name)
print(m1.get_income())

m1.set_income(150000)
print(m1.get_income())


# 12-misol
class Employee:
    def __init__(self, fullname, experience):
        self.fullname = fullname
        self.__experience = experience

    def get_experience(self):
        return self.__experience

    def set_experience(self, new_experience):
        self.__experience = new_experience

e1 = Employee('Rustam Aliyev', 3)

print(e1.fullname)
print(e1.get_experience())

e1.set_experience(5)
print(e1.get_experience())


# 13-misol
class School:
    def __init__(self, school_name, students):
        self.school_name = school_name
        self.__student = students

    def get_students(self):
        return self.__student

    def set_students(self, new_student):
        self.__student = new_student

s1 = School('45-maktab', 800)

print(s1.school_name)
print(s1.get_students())

s1.set_students(1000)
print(s1.get_students())


# 14-misol
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.__pages = pages

    def get_pages(self):
        return self.__pages

    def set_pages(self, new_pages):
        self.__pages = new_pages

b1 = Book('Python asoslari', 250)

print(b1.title)
print(b1.get_pages())

b1.set_pages(300)
print(b1.get_pages())


# 15-misol
class Company:
    def __init__(self, company_name, workers):
        self.company_name = company_name
        self.__workers = workers

    def get_workers(self):
        return self.__workers

    def set_workers(self, new_worker):
        self.__workers = new_worker

c1 = Company('Google', 150000)

print(c1.company_name)
print(c1.get_workers())

c1.set_workers(200000)
print(c1.get_workers())
