import argparse


characteristics = ['фамилия', 'имя', 'отчество', 'организация', 'раб-ном', 'лич-ном']

class InvalidChar(Exception):
    pass

def edit(id, attr):
    changed_char = input('Введите данные для заданной характеристики: ')
    with open('data/' + id + '.txt', 'r') as file:
        file_lines = file.readlines()
    with open('data/' + id + '.txt', 'w') as file:
        for line in range(len(file_lines)):
            if file_lines[line].lower().startswith(attr):
                file_lines[line] = attr+': ' + changed_char+'\n'
            file.write(file_lines[line])

parser = argparse.ArgumentParser(prog='Интерфейс для поиска записей')
parser.add_argument('id', type=str, help='id объекта')
parser.add_argument('attr', type=str, help='Изменение определенной характеристики(фамилия, имя, отчество,'
                                          ' организация, раб-ном, лич-номм)')
id = parser.parse_args().id
attr = parser.parse_args().attr.lower()
if attr in characteristics:
    edit(id, attr)
else:
    raise Exception('Введена неправильная характеристика')