#!/usr/bin/env python3

import os 

if __name__ == '__main__':

    length = 3

    folder_list = next(os.walk('.'))[1]

    for folder in folder_list:

        if folder.isdigit():
            os.rename(folder, folder.rjust(length, '0'))
