# age = -1
# human=input("Введіть свій вік ")
# if human.isnumeric():
#     age = int(human)
#
# if age == -1:
#     print("Число було введено невірно")
# elif age>0 and age<7:
#     print("Де твої батьки")
# elif age>7 and age<16:
#     print('це фільм для дорослих')
# elif age>65:
#     print("Покажіть пенсійне посвідчення")
# else:
#     print("А, квитків вже немає")
# Мой вариант
#
# age = -1
# client=input("Введіть свій вік ")
# if client.isnumeric():
#     age = int(client)
#
# if 1>age or age<155:
#     print("Вы ДОЛБОЕБ")
# elif -1<age<=7:
#     print("Де твої батьки?")
# elif 7<age<=16:
#     print("Це кіно для дорослих")
# elif 16<age<=64:
#     print("А, квитки закінчилися")
# elif 64<age<=150:
#     print("Ваше пенсійне посвідчення")

age = -1
user_data = input("Введіть свій вік\n")
if user_data.isnumeric():
    age=int(user_data)
if age==-1:
    print("Введіть правильне значенни")
elif age>120:
    print("Так довго не живуть!")
elif len(user_data)==2 and user_data[0]==user_data[1]:
    print("Як цікаво")
elif age in range(0,7):
    print("Де твої батьки?")
elif age in range(7,16):
    print("Це фільм для дорослих!")
elif age in range():
    print("Покажіть пенсійне посвідчення!")
else:
    print("А білетів вже немає!")









# Pidrilo=input("Введіть свій текст ")
# if Pidrilo.isalpha():
#     print("он гусь")
# else:
#     print("он красавчик")
#
# if Pidrilo.isupper():
#     print("он гусь")
# else:
#     print("он красавчик")
#
# if Pidrilo.isdigit():
#     print("он гусь")
# else:
#     print("он красавчик")
#
# if Pidrilo.startswith("прив"):
#     print("он гусь")
# else:
#     print("он красавчик")
#
# Pidrilo = "МАЛЕНЬКИЙ ПРИНЦ — ИЗВЕСТНЕЙШЕЕ ТВОРЕНИЕ АНТУАНА ДЕ СЕНТ-ЭКЗЮПЕРИ УВИДЕЛО СВЕТ В 1943 ГОДУ."
# Pidrilo = Pidrilo.upper()
# print(Pidrilo)
#
#
# Pidrilo = "МАЛЕНЬКИЙ ПРИНЦ — ИЗВЕСТНЕЙШЕЕ ТВОРЕНИЕ АНТУАНА ДЕ СЕНТ-ЭКЗЮПЕРИ УВИДЕЛО СВЕТ В 1943 ГОДУ."
# Pidrilo = Pidrilo.lower()
# print(Pidrilo)
#
#
# Pidrilo = "МАЛЕНЬКИЙ ПРИНЦ — ИЗВЕСТНЕЙШЕЕ ТВОРЕНИЕ АНТУАНА ДЕ СЕНТ-ЭКЗЮПЕРИ УВИДЕЛО СВЕТ В 1943 ГОДУ."
# Pidrilo = Pidrilo.title()
# print(Pidrilo)

