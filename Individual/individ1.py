#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sentence = input("Введите преддложение: ")
count = 1

for char in sentence:
    if count % 3 == 0:
        print(char)
    count += 1