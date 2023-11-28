#задание№1
children_list = list()
while True:
 admin = input("что хотите сделать/добавить/удалить/посмотреть список учеников/выйти")
 if admin =="добавить":
  student_name = input("введите имя ученика-")
  student_year = input("введите возраст ученика-")
  student_class = input("ВВЕДИТЕ КЛАСС УЧЕНИКА(букву)")
  print(f"{student_name}:{student_year}:{student_class} добавлен в список школы")

 elif admin == "удалить":
  student_name = input("введите имя ученика-")
  student_year = input("введите возраст ученика-")
  student_class = input("ВВЕДИТЕ КЛАСС УЧЕНИКА(букву)")
  print(f"{student_name}:{student_year}:{student_class} удален из списка школы")

 elif admin == "посмотреть список учеников":
  print(children_list)

 else:break
# задание№2
x1 =int(input("введите число"))
y2 =int(input("введите число"))
a = lambda x,y:x1 + y2
print(a(x1,y2))