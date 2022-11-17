# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# types

# int, float

# bool

# str

name="Stas"
age= 29

my_str= "Привіт! Мене звати %s, мені %s років" % (name, age)
print(my_str)
tpl="Привіт! Мене звати {}, мені {} років"
my_str=  tpl.format (name, age)
print(my_str)


tpl="Привіт! Мене звати {name_var}, мені {age_var} років"
my_str=  tpl.format (name_var=name, age_var=age)
print(my_str)

# f-sting
my_str=f"Привіт! Мене звати {name}, мені {age} років"
print(my_str)

print("Hello" in my_str)

print("Привіт" in my_str)

my_str=f"Привіт! Мене звати {name}, мені {age} років"