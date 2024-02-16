#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sentence = input("Введите предложение: ")
count = 1

for i in range(len(sentence)):
    if sentence[i] == 'щ' or sentence[i] == 'ч' or sentence[i] == 'Щ' or sentence[i] == 'Ч':
        if sentence[i + 1] == 'у':
            print('Есть буквосочетание чу или щу')
            print('Порядковый номер первого буквосочетания -', count)
            break
    count += 1
