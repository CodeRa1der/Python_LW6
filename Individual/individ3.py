#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word = input("Введите слово с точкой в конце: ")
    replacer = 'a'
    for i in range(len(word)):
        if i == 5:
            print('Новое слово:', word[:5] + replacer + word[5:])
