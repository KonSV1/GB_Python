#3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1 (isinstance())
# - список: [], ищем: "123", ответ: -1


def find_string(list: list, num):
    count = 0
    for i in range(len(list)):
        if num == list[i]:
            count +=1
            if count == 2:
                return i
    return -1
            
lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
num = input("Write string: ")

print(find_string(lst, num))





def task3(sp: list, word: str) -> int:
    if word not in sp:
        return -1
    n1 = sp.index(word)
    return sp.index(word, n1 + 1) if word in sp[n1 + 1:] else -1

