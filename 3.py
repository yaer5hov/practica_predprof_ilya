import csv
with open('scientist.csv', encouding = 'utf - 8') as file:
    header = list(csv.DictReader(file, delimiter = ',', quotechar = '"'))
    data = sorted(header, key, lambda x: x['ScientistName'])
    ''' Описание файла
    header - считываем файл и записываем значение через запятую
    data = сортирум header по ScientistName
    '''
        
id_project = input()
while id_project != 'эксперимент':
    id_project = int(id_project)
    for el in data:
        if int(el['ScientistName']) == id_project:
            name, surname,otchectvo = el['ScientistName'].split()
            print(f'Ученый {{surname}.{name[0]}.{otchectvo[0]}} создал препарат: {preparation} - {date}')
        else:
            print('В этот день ученые отдыхали')
    id_project = input()
