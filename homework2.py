# age = -1
# Pidrilo=input("Введіть свій вік ")
# if Pidrilo.isnumeric():
#     age = int(Pidrilo)
#
# if age == -1:
#     print("Число було введено невірно")
# elif age>0 and age<7:
#     print("Де твої батьки")
# elif age>7 and age<16:
#     print(f'це фільм для дорослих')
# elif age>65:
#     print(f"Покажіть пенсійне посвідчення")
# else:
#     print(f"А, квитків вже немає")
#
Pidrilo=input("Введіть свій текст ")
if Pidrilo.isalpha():
    print("он гусь")
else:
    print("он красавчик")

if Pidrilo.isupper():
    print("он гусь")
else:
    print("он красавчик")

if Pidrilo.isdigit():
    print("он гусь")
else:
    print("он красавчик")

if Pidrilo.startswith("прив"):
    print("он гусь")
else:
    print("он красавчик")

Pidrilo = "МАЛЕНЬКИЙ ПРИНЦ — ИЗВЕСТНЕЙШЕЕ ТВОРЕНИЕ АНТУАНА ДЕ СЕНТ-ЭКЗЮПЕРИ УВИДЕЛО СВЕТ В 1943 ГОДУ."
Pidrilo = Pidrilo.upper()
print(Pidrilo)


Pidrilo = "МАЛЕНЬКИЙ ПРИНЦ — ИЗВЕСТНЕЙШЕЕ ТВОРЕНИЕ АНТУАНА ДЕ СЕНТ-ЭКЗЮПЕРИ УВИДЕЛО СВЕТ В 1943 ГОДУ."
Pidrilo = Pidrilo.lower()
print(Pidrilo)


Pidrilo = "МАЛЕНЬКИЙ ПРИНЦ — ИЗВЕСТНЕЙШЕЕ ТВОРЕНИЕ АНТУАНА ДЕ СЕНТ-ЭКЗЮПЕРИ УВИДЕЛО СВЕТ В 1943 ГОДУ."
Pidrilo = Pidrilo.title()
print(Pidrilo)

