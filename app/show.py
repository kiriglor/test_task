import argparse

def show(id):
    with open('data/'+id+'.txt', 'r') as file:
        print(file.read())

parser = argparse.ArgumentParser(prog='Интерфейс для вывода записи на экран')
parser.add_argument('id', type=str, help='id объекта')
arg = parser.parse_args().id
show(arg)
