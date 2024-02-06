d = {'day' : 22, 'month' : 6, 'year' : 2015}

print("||".join(d.keys()))

a = 5
b = 3+2
print(id(a)) # идентификаторы оказались одинаковыми
print(id(b))

list_1 = ['a', 'b', 'c']
list_2 = list_1  # значения и идентификаторы равны
list_3 = list(list_1) # значения равны но идентификаторы будут разными
print(list_1)
print(list_2)
print(list_3)

print(list_1 == list_2)
print(list_1 == list_3)

print(list_1 is list_2)
print(list_1 is list_3)

L = ['Hello', 'world']
M = L
print(M is L)
M.append('!') # изменение в М перенеслов в L
print(L)

M = L.copy()  # ПОЭТОМУ копируем списки чтоб изменения не переносились
print(M is L)

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
shopping_center[-1].append("Uniqlo") # сам кортеж не изменяем но у нас есть список внутри кортежа
print(shopping_center)


text = input("Введите текст:")
unique = list(set(text))
print("Количество уникальных символов: ", len(unique))
