#Время не ждет
import time
#Именниник
name = 'Степан'
#Коллектив
list_collectiv = list()
list_collectiv.append('Сергей')
list_collectiv.append('Вова')
list_collectiv.append('Толя')
list_collectiv.append('Виталя')
list_collectiv.append('Оля')
list_collectiv.append('Юля')



def happy_bithday(name):

    print(f'С днем рождения , {name} !!!')
    time.sleep(1)
    print('Пусть планы сбываются, пусть мечты - мечтаются, а потом разделяются на мелкие планы и тоже осуществляются.')
    time.sleep(1)
    print('Пусть границы всегда будут открыты, а над головой - только светлое яркое небо.')
    time.sleep(1)
    print('Пусть будут силы и желание двигаться и работать, а отдых случается гармонично и тогда, когда ты того хочешь.')
    time.sleep(1)

def pozdravlenie_collectiva(list_collectiv):
    print(f' Наш веселый коллектив: {list_collectiv}')

def check_reaction(name):
    print(f' {name}, введи реакцию:')
    reaction = str(input())

    result = True
    print(reaction)
    if ')' in reaction:
        print(reaction)
        print('Поздравление получилось ))) ')
        pozdravlenie_collectiva(list_collectiv)
        for i in list_collectiv:
            print(f'{i}:')
            print(reaction)
        result = False

    return result

if __name__ == '__main__':
    happy_bithday(name)

    res = True
    while res:
        res = check_reaction(name)









