a = True
while a:
    vibor = int(input("""Выбери номер опки: 
0-Выход
1-Запись
2-Удаление\n"""))
    if vibor == 0:
        a = False

    if vibor == 1:
        rasp = input('Что ты хочешь сделать сегодня? ')
        with open('Rasp.txt', 'a', encoding='utf-8') as raspicuka:
            raspicuka.write(rasp + '\n')


    elif vibor == 2:
        with open('Rasp.txt', 'w', encoding='utf-8') as raspicuka:
            pass
            print('Все данные были удалены')
