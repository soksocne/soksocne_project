from ast import While
import csv
import schedule
import time

def write_csv():
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    with open('users.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')
        writer.writerow(
            (name, age)
        )
    answ = input('Cont? y/n: ')
    if answ == 'y':
        write_csv()
    else:
        print('stop!')
    
def mailing():
    with open('users.csv', 'r') as csv_file:
        data = csv_file.readlines()
        names = [i.replace('\n', '') for i in data]
        for i in names:
            name = i.split('/')
            if int(name[-1]) >= 18:
                print(f'Скидки сегодня! {name[0]}')

schedule.every(3).seconds.do(mailing)

while True:
    schedule.run_pending()
    time.sleep(1)