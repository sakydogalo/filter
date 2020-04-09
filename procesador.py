#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Name: Saky
# Mail: sakydogalo@gmail.com
#
#

import csv

from archivo import Archivo

class Procesador(Archivo):
    def __init__(self):
        self.datos_procesados = []
        self.campos_procesados = []
        super().__init__()

    def enumerar(self):
        self.campos_procesados.append('id')
        self.campos_procesados += self.campos
        i = 1
        for row in self.datos:
            self.datos_procesados.append([i] + row)
            i +=1

    def guardar_procesado(self,
        csv_:str,
        encoding: str,
        delimiter: str):

        f = open(csv_, 'w',encoding=encoding)
        with f:
            writer = csv.writer(f,delimiter=delimiter)
            writer.writerow(self.campos_procesados)
            for row in self.datos_procesados:
                writer.writerow(row)   