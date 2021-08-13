#Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
#в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
#Например:
#>>> thesaurus("Иван", "Мария", "Петр", "Илья")
my_list = {}
def thesaurus(*names):
    for name in names:
        names = ' '.join(name)
        for i in names[0]:
            my_list.setdefault(i, []).append(name)
    return my_list

thesaurus()
thesaurus('Исус', 'Миша', 'Игнат', 'Полина', 'Юля', 'Кирилл', 'Томара')
print(thesaurus())
