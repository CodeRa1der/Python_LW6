#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sentence = input("Введите преддложение: ")
    count = 1

    for char in sentence:
        if count % 3 == 0:
            print(char)
        count += 1