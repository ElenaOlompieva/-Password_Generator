import random
import time
#библиотека для работы с буфером обмена
import pyperclip

Letter = "abcdefghijklmnopqrstuvwxyz"
Letter_C = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Number = "0123456789"
Symbol = "`!@#$%^&*_-+='|(){}[]:;<>,./\?"

all = Letter + Letter_C + Number + Symbol
Length = 18
Password = "".join(random.sample(all,Length))

print("Идет генерация пароля..")
time.sleep(3)

#записываем пароль в буфер обмена
pyperclip.copy(Password)

#открываем файл на добавление
with open('data.txt', 'a') as fp:
#записываем пароль из буфера обмена в текстовый файл
    fp.write(pyperclip.paste() + '\n')
    
#вывод пароля на экран
print("Ваш пароль готов:")
print(Password)