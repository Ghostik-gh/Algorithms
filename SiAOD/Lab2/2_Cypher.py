# Задание №2
'''
Дек содержит последовательность символов для шифровки сообщений. 
Дан текстовый файл, содержащий зашифрованное сообщение.
Пользуясь деком, расшифровать текст. 
Известно, что при шифровке каждый символ сообщения 
заменялся следующим за ним в деке по часовой стрелке через один.
01234
Hello
lloHe
'''

import re


def encrypt(key: str, text: str):
    msg = ""
    while len(text) > 0:
        if re.search("\W", text[0]):
            msg = msg + text[0]
            text = text[1:]
            continue
        for i in range(len(key)):
            if text[0].lower() == key[i]:
                msg = msg + key[(i+2) % len(key)]
                text = text[1:]
                break
    return msg


def decrypt(key: str, text: str):
    msg = ""
    while len(text) > 0:
        if re.search("\W", text[0]):
            msg = msg + text[0]
            text = text[1:]
            continue
        for i in range(len(key)):
            if text[0].lower() == key[i]:
                msg = msg + key[(i - 2 + len(key)) % len(key)]
                text = text[1:]
                break
    return msg


if __name__ == "__main__":
    with open('Lab2\input2.txt', 'r') as f:
        # Может быть алфавит в любом порядке
        deque = f.readline().strip()
        text = f.read().strip()
    print(text)
    print(encrypt(deque, text))
    print(decrypt(deque, encrypt(deque, text)))
