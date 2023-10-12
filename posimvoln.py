text = "нанана нананоо"
strr = "нанано"

k = 0

for i, t in enumerate(text):
    if t == strr[k]:#если совпадение произошло
        if k == len(strr) - 1:
            print("шаблон найден")
            break
        else:
            k += 1

    elif i == len(text) - 1:#дошли до конца и ничего не нашли
        print("шаблон не найден")

    else:
        k = 0

#O(n*m)кол-во символов в тексте на кол-во символов в образце