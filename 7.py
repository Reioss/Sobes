#Напишите любую функцию, где задано значение по умолчанию (название функции и значение на ваш выбор).
i = 5

def f(arg=i):
    print(arg)

i = 6
f() # напечатает 5.
