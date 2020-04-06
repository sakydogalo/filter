#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#

import csv


with open('FACTURACION.csv',encoding='ISO-8859-1') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    lineas = []

    for row in csv_reader:
        if line_count == 0:
            campos = row
        else:
            lineas.append(row)
        line_count +=1
    print('lineas:',line_count)
    print(campos)
    print(lineas)    
