#задание№1
my_contact = ["САША","МАША","КОЛЯ","ТАНЯ"]
CHOIS = int(input("1-add" "2-remove" "3-clear"))
if CHOIS == 1:
    new_contact =input("напишите новый контакт")
    my_contact.append(new_contact)
    print(f"ваш контакт {new_contact} добавлен")
elif CHOIS ==2:
    contact =input("напишите контакт который хотите удалить")
    my_contact.remove(contact)
    print(f"ваш контакт {contact} удален")
else:CHOIS ==3
my_contact.clear()
print("все контакты удалены")
#задание№2
слово = input("введите слово")
if слово==слово[::-1]:
    print("это полиндром")
else:
    print("это не полиндром")
#задание№3
числа = int(input("введите число и я вам выдаду таблицу на него"))
print(f"тблица умножения на :{числа}")
for число in range(1,11):
    print(числа,"*",число,"=",числа*число)

