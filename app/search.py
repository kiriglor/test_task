import os
import argparse


characteristics = ['фамилия', 'имя', 'отчество', 'организация', 'раб-ном', 'лич-ном']


def search(args: list):
    files = os.listdir('data')
    titles = {}
    id_list=[]
    for arg in args:
        titles[arg] = (input('Введите ' + arg + ': '))
    # Поиск данных в формате ключ: значение Среди всех данных
    for file_name in files:
        with open('data/' + file_name, 'r') as file:
            file_lines = file.readlines()
            check_arguments= True
            for arg in args:
                check_argument = False
                for line in file_lines:
                    if line.startswith(arg) and line.endswith(titles[arg]+'\n'):
                        check_argument = True
                if check_argument == False:
                    check_arguments=False
            if check_arguments:
                id_list.append(file_name)
    for id in id_list:
        print(id[0:-4])


parser = argparse.ArgumentParser(prog='Интерфейс для поиска записей')
parser.add_argument('args', type=str, help='Атрибуты характеристик записей (Вводить через пробел: фамилия, имя, отчество,'
                                          ' организация, раб-ном, лич-номм) ')
args = parser.parse_args().args.split(' ')
to_pop = []

for i in range(len(args)):
    args[i] = args[i].lower()
    if args[i] not in characteristics:
        to_pop.append(i)

for pop in range(len(to_pop), 0, -1):
    print('hi')
    args.pop(to_pop[pop])

search(args)
