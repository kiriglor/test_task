import datetime


def create():
    '''
    Функция для создания текстовой записи
    '''
    lst = {'Фамилия': False,
           'Имя': False,
           'Отчество': False,
           'Организация': False,
           'Рабочий номер': False,
           'Личный номер': False}

    for title in lst.keys():
        lst[title] = input(title + ': ')
    date_time = datetime.datetime.now()
    format = '%Y-%m-%d-%H-%M'
    string = date_time.strftime(format)
    
    with open('data/id.txt', 'r') as id:
        file_id = id.read()
    with open('data/id.txt', 'w') as id:
        id.write(str(int(file_id)+1))

    with open('data/'+file_id+'.txt', 'w') as file:
        for i in lst.keys():
            file.write(i + ': '+lst[i]+'\n')
        file.write('Дата создания: ' + string + '\n')
    id.write(str(int(file_id)+1))


create()

