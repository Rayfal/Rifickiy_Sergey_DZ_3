#1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский
# язык. Например:
#>>> num_translate("one")
#"один"
#>>> num_translate("eight")
#"восемь"
#Если перевод сделать невозможно, вернуть None.
#Подумайте, как и где лучше хранить информацию, необходимую для перевода:
#какой тип данных выбрать, в теле функции или снаружи.

#num_translata(number_rus)
def num_translate_rus(key):
    for key, val in my_list.items():
        if key == number:
           return val
        else:
            return None

def num_translate_eng(val):
    for key, val in my_list.items():
        if val == number:
           return key
        else:
            return None
my_list = {
    'Один' : 'One',
    'Два' : 'Two',
    'Три': 'Three',
    'Четыре': 'Four',
    'Пять': 'Five',
    'Шесть': 'Six',
    'Семь': 'Seven',
    'Восемь': 'Eight',
    'Девять': 'Nine',
    'Десять': 'Ten'
}
number = input('Введите чесло от 1 - 10 на русском: ')
print(num_translate_rus(number))

number = input('Введите чесло от 1 - 10 на английском: ')
print(num_translate_eng(number))
