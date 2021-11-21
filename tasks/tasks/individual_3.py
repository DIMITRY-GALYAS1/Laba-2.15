#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Написать программу, с помощью которой можно получить доступ
к названиям и путям всех подпапок и файлов, относящихся к
заданному каталогу.
"""

import os


if __name__ == "__main__":
    for root, directories, files in os.walk(r"C:\Users\lizeq\Laba-2.12\tasks"):
        print(root)
        for directory in directories:
            print(directory)
        for file in files:
            print(file)
