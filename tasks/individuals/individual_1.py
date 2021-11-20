#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Написать программу, которая считывает текст из файла и
выводит на экран только предложения, содержащие введенное
с клавиатуры слово.
"""


if __name__ == '__main__':
    with open('text1.txt', 'r', encoding="utf-8") as z:
        sentences = z.readlines()

    word = input("Введите слово: ")

    for sentence in sentences:
        if word in sentence:
            print(sentence)
