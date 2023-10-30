import json
import os
import csv
balance = 50
Results = [{
    'balance' : 0,
    'username': ''
}]
CSV = "Table.CSV"
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Пожалуйста, введите целое число.")

def load_game():
    try:
        with open('output.json', 'r') as file:
            data = json.load(file)
            return data.get("balan", balance)
    except FileNotFoundError:
        return balance
    
def save_ToCSV():
    Results[0]['balance'] = balance
    fieldnames = ['username', 'balance']
    with open(CSV, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(Results)

def delete_saved_game():
    try:
        with open('output.json', 'r') as file:
            data = json.load(file)  
        if 'balan' in data:
            del data['balan']
            with open('output.json', 'w') as file:
                json.dump(data, file, indent=4)
            print("Сохраненная игра удалена.")            
            with open(CSV, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['username', 'balance'], delimiter=";")
                writer.writeheader()
                writer.writerows([{'username': '', 'balance': 0}])
        else:
            print("Нет сохраненной игры для удаления.")
        main()
    except FileNotFoundError:
        print("Нет сохраненной игры для удаления.")
        num()

def num4():
    global balance
    balance = load_game()
    print("\nВы попали в мир, полный загадок и волшебства!")
    print("Выберите своего персонажа:\n1.Мина \n2.Александр ")
    name_1 = get_integer_input("")
    
    my_list = ["Мину", "Александра"]
    if name_1 == 1:
       print(f"\nВы будете путешествовать за {my_list[0]}. Баланс: {balance}")
       num()
    elif name_1 == 2:
       print(f"\nВы будете путешествовать за {my_list[1]}. Баланс: {balance}")
       num()
    else:
        print("Пожалуйста, выберите 1 или 2.")
        return num4()
def num():
    print("Выберите, куда хотели бы отправиться:\n1.Город\n2.Лес\n3.Горы\n4.Сохранить игру и выйти\n5.Удалить сохранение")
    name_2 = get_integer_input("")
    if name_2 == 1:
        num1()
    elif name_2 == 2:
        num2()
    elif name_2 == 3:
        num3()
    elif name_2 == 4:
        data = {
        "balan": balance
        }
        with open('output.json', 'w') as file:
            json.dump(data, file, indent=4)
    elif name_2 == 5:
        delete_saved_game()
    else:
        print("Пожалуйста, выберите 1 или 2 или 3 или 4 или 5.")
        return num()
def num1():
    print("\nВы отправились в город")
    print("Пока вы шли, вы увидели раненного незнакомца. Поможете ему?\n1.Да\n2.Нет\n3.Сохранить игру и выйти")
    name_3 = get_integer_input("")
    while name_3 != 1 and name_3 != 2 and name_3 != 3:
        print("Неправильный выбор. Пожалуйста, введите 1 или 2 или 3.")
        name_3 = get_integer_input("")
    if name_3 == 1:
        print("\nВы помогли ему и он рассказал вам, что недалеко отсюда находиться лавка\nОтправитесь туда?\n1.Да\n2.Нет\n3.Сохранить игру и выйти")
        name_4 = get_integer_input("")
        while name_4 != 1 and name_4 != 2 and name_4 != 3:
            print("Неправильный выбор. Пожалуйста, введите 1 или 2 или 3.")
            name_4 = get_integer_input("")
        if name_4 == 1:
            print("\nВы добрались до лавки и заметили, что в ней продаются травы. Хотите купить их?\n1.Да\n2.Нет\n3.Сохранить игру и выйти")
            answer = get_integer_input("")
            while answer != 1 and answer != 2 and answer != 3:
                print("Неправильный выбор. Пожалуйста, введите 1 или 2 или 3.")
                answer = get_integer_input("")
            if answer == 1:
                global balance
                print(f"\nВаш баланс: {balance}")
                cena = {'1.Взрывоопасные травы': 100, '2.Травы для восстановления силы' : 25, '3.Травы для воскрешения': 50}
                for key,value in cena.items(): 
                    print(key, ':', value)
                answer_1 = get_integer_input("")
                while answer_1 != 1 and answer_1 != 2 and answer_1 != 3:
                    print("Неправильный выбор. Пожалуйста, введите 1 или 2 или 3.")
                    answer_1 = get_integer_input("")
                if answer_1 == 1:
                    if balance > 100:
                        balance = balance - 100
                        print(f"\nВаш баланс: {balance}")
                        print("\nИз-за своей неуклюжести вы уронили травы и они взорвались, пострадала лавка. Торговец заставил вас возместить ущерб")
                        balance = balance - 25
                        print(f"\nВаш баланс: {balance}")
                        print("Вы прочесали весь город, но ничего не нашли, поэтому решили вернуться домой.\nПоздравляю, вы избежали все опасные ситуации и прошли игру!")
                        save_ToCSV()
                    elif balance <= 100:
                        print("\nУ вас не хватает монет. Торговец разозлился и сильно ударил вас по голове.\nВы умерли от кровоизлияния.\nИгра закончена.")
                        save_ToCSV()
                elif answer_1 == 2:
                    if balance >= 25:
                        balance = balance - 25
                        print(f"\nВы купили травы для восстановления силы, но оно оказалось неисправным. Самое бесполезное приобритение.\nВаш баланс: {balance}")
                        print("Вы вышли на улицу и прочесали весь город, но ничего не нашли, поэтому решили вернуться домой.\nПоздравляю, вы избежали все опасные ситуации и прошли игру!")
                        save_ToCSV()
                    elif balance < 25:
                        print("\nУ вас не хватает монет. Торговец разозлился и сильно ударил вас по голове.\nВы умерли от кровоизлияния.\nИгра закончена.")
                        save_ToCSV()
                elif answer_1 == 3:
                    if balance >= 50:
                        balance = balance - 50
                        print(f"\nВаш баланс: {balance}. Вы купили травы для восрешения и решили испробовать, но они оказалось отравленными, и вы умерли.\nИгра закончена")
                        save_ToCSV()
                    elif balance < 50:
                        print("\nУ вас не хватает монет. Торговец разозлился и сильно ударил вас по голове.\nВы умерли от кровоизлияния.\nИгра закончена.")
                        save_ToCSV()
            elif answer == 2:
                print("\nВас не заинтересовали травы, и вы ушли из лавки")
                print("Вы прочесали весь город, но ничего не нашли, поэтому решили вернуться домой.\nПоздравляю, вы избежали все опасные ситуации и прошли игру!")
                save_ToCSV()
            elif answer == 3:
                data = {'balan': balance
                }
                with open('output.json', 'w') as file:
                    json.dump(data, file, indent=4)
        elif name_4 == 2:
            print("\nВы решили пойти в лес")
            num2()   
        elif name_4 == 3:
            data = {
            'balan': balance
            }
            with open('output.json', 'w') as file:
                json.dump(data, file, indent=4)   
    elif name_3 == 2:
        balance = balance + 100
        print(f"\nВы забрали его деньги и решили пойти в лес \nВаш баланс: {balance}")
        num2()
    elif name_3 == 3:
        data = {
        'balan': balance
        }
        with open('output.json', 'w') as file:
            json.dump(data, file, indent=4)

def num2():
    print("\nПока вы шли в лес, в далеке вы увидели заброшенный дом.\nОтправитесь туда?\n1.Да\n2.Нет\n3.Сохранить игру и выйти")
    name_5 = get_integer_input("")
    while name_5 != 1 and name_5 != 2 and name_5 != 3:
        print("Неправильный выбор. Пожалуйста, введите 1 или 2 или 3.")
        name_5 = get_integer_input("")
    if name_5 == 1:
        print("\nПеред вами предстал огромный мужчина по имени Геннадий.")
        print("Он предложил купить вам меч. Согласитесь покупать?\n1.Да\n2.Нет\n3.Сохранить игру и выйти")
        name_6 = get_integer_input("")
        while name_6 != 1 and name_6 != 2 and name_6 != 3:
            print("Неправильный выбор. Пожалуйста, введите 1 или 2 или 3.")
            name_6 = get_integer_input("")
        if name_6 == 1:
            print("\nУ вас не хватает монет. Геннадий разгневался и схватил вас. Он запер вас в доме, навсегда...\nИгра закончена. ")
            save_ToCSV()
        elif name_6 ==2:
            print("\nГеннадий разгневался и схватил вас. Он запер вас в доме.\nИгра закончена.")
            save_ToCSV()
        elif name_5 == 3:
            data = {
            'balan': balance
            }
            with open('output.json', 'w') as file:
                json.dump(data, file, indent=4)
    elif name_5 == 2:
        print("\nВы продолжили своё путешествие.")
        num3()
    elif name_5 == 3:
        data = {
        'balan': balance
        }
        with open('output.json', 'w') as file:
            json.dump(data, file, indent=4)
def num3():
    print("\nВы отправились в горы. По дороге наверх, вы обнаружили сундук. Открыть его?\n1.Да\n2.Нет\n3.Сохранить игру и выйти")
    name_7 = get_integer_input("")
    while name_7 != 1 and name_7 != 2 and name_7 != 3:
        print("Неправильный выбор. Пожалуйста, введите 1 или 2 или 3.")
        name_7 = get_integer_input("")
    if name_7 == 1:
        global balance
        balance = balance + 50
        print(f"\nВ сундуке были деньгии. Баланс: {balance}")
        print("После долгого подъёма вы наконец-то наверху. Хотите отдохнуть?\n1.Да\n2.Нет\n3.Сохранить игру и выйти")
        name_8 = get_integer_input("")
        while name_8 != 1 and name_8 != 2 and name_8 != 3:
            print("Неправильный выбор. Пожалуйста, введите 1 или 2 или 3.")
            name_8 = get_integer_input("")
        if name_8 == 1:
            print("\nВы уснули в горах.\nИ пока вы спали вас укусила змея. В результате вы погибли.\nИгра закончена.")
            save_ToCSV()
        elif name_8 == 2:
            print("\nВы продолжили своё путешествие")
            num1()
        elif name_8 == 3:
            data = {
            'balan': balance
            }
            with open('output.json', 'w') as file:
                json.dump(data, file, indent=4)
    elif name_7 == 2:
        print("\nВы продолжили своё путешествие по горам.")
        print("После долгого подъёма вы наконец-то наверху. Хотите отдохнуть?\n1.Да\n2.Нет\n3.Сохранить игру и выйти")
        name_9 = get_integer_input("")
        while name_9 != 1 and name_9 != 2 and name_9 != 3:
            print("Неправильный выбор. Пожалуйста, введите 1 или 2 или 3.")
            name_9 = get_integer_input("")
        if name_9 == 1:
            print("\nВы уснули в горах. И пока вы спали вас укусила змея. В результате вы погибли.\nИгра закончена.")
            save_ToCSV()
        elif name_9 == 2:
            print("\nВы продолжили своё путешествие")
            num1()
        elif name_9 == 3:
            data = {
            'balan': balance
            }
            with open('output.json', 'w') as file:
                json.dump(data, file, indent=4)
    elif name_7 == 3:
        data = {
        'balan': balance
        }
        with open('output.json', 'w') as file:
            json.dump(data, file, indent=4)


def main():
    print("Здравствуйте, хотите сыграть в игру?\n1.Да\n2.Нет")
    name = get_integer_input("")
    if name == 1:
        Results[0]['username'] = input('Введите свое имя:')
        num4()
    elif name == 2:
        print("Всего хорошего! Обязательно найдите время, чтобы пройти эту замечательную игру.")
    else:
        print("Пожалуйста, выберите 1 или 2.")
        return main()
main()

