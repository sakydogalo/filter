#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
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
    # print number of lines of the csv
    print('Lineas:',line_count)
    #print fields of the csv
    print('Campos: ',campos)
    #print the first row of the csv
    print('Primera linea: ',lineas[0])
