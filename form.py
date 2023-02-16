import json

OPEN_TIME = 10
CLOSE_TIME = 21

def check_date(str_date):
    if len(str_date.split("-")) != 3:
        return False
    y, m, d = str_date.split("-")
#    if len(year) != 4 or len(month) != 2 or len(day) != 2:
#        return False
#    if not(year.isdigit() and month.isdigit() and day.isdigit()):
    if y.isdigit() and m.isdigit() and d.isdigit():
        y, m, d = int(y), int(m), int(d)
    if 2000 <= y <= 3000 and 1 <= m <= 12 and 1 <= d <= 31:
        return True
    else:
        return False
def check_int(number, begin, end):
    if not(number.isdigit()):
        return False
    number = int(number)
    return begin <= number <= end


def ask_int(begin, end):
    number = None
    while number is None:
        temp = input()
        if check_int(temp, begin, end):
            number = int(temp)
        else:
            print("Введена не коректная дата")


def ask_user():
    print("Введите время ожидания очереди (в часах):")
    # wait = None
    # while wait is None:
    #     temp = input()
    #     if temp.isdigit() and 0 <= int(temp) <= 24:
    #         wait = int(temp)
    #     else:
    #         print("Введена не корректное значение!")
    wait = ask_int(0, 12)

    print(f"Введите час, в котором вы посещали МФЦ? (от {OPEN_TIME} до {CLOSE_TIME})")

    # hour = None
    # while hour is None:
    #     temp = input()
    #     if temp.isdigit() and OPEN_TIME <= int(temp) <= CLOSE_TIME:
    #         hour = int(temp)
    #     else:
    #         print("Введите коррректное значение!")
    hour = ask_int(OPEN_TIME, CLOSE_TIME)
    print("Введите дату посещения (в формате YYYY-MM-DD):")

    date = None
    while date is None:
        temp = input()
        if check_date(temp):
            date = temp
        else:
            print("Введите коррректное значение!")

    return {
            "wait" : wait,
            "hour" : hour,
            "date" : date
    }
def load_info():
    with open("info.json") as f:
        info = json.load(f)
    return info

def load_stat():
    with open("stat.json") as f:
        stat = json.load(f)
    return stat

def save_stat(stat):
    with open("stat.json", "w") as f:
        stat = json.dump(stat, f)

def save_info(info):
    with open("info.json", "w") as f:
        json.dump(info, f)


def main():
    stat = load_info()
    while True:
        stat.append(ask_user())
        print("Продолжить заполнять анкету (Да/Нет)?")

        temp =  input()
        if temp.lower() != "Да":
            break

    save_info(stat)


main()


def ask_date():
    print("Введите дату:")
    date = None
    while date is None:
        temp = input()
        if check_date(temp):
            date = temp
        else:
            print("Введена не коректная дата")
    return date







def save_info(info):
    with open("info.json", "w") as f:
        json.dump(info, f)






