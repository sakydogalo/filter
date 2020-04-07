#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Name: Saky
# Mail: sakydogalo@gmail.com
#
# 

import csv

from log import Log

class Archivo(object):
    
    def __init__(self):
        self.datos  = []
        self.campos = []
        self.line_count = 0


    def abrir(self,
        csv_:str,
        encoding: str,
        delimiter: str):
        Log.logger.info('(Abrir):')
        Log.logger.info('\tArchivo     :"' + csv_ +'"')
        Log.logger.info('\tCodificación:"' + encoding +'"')
        Log.logger.info('\tDelimitador :"' + delimiter +'"')
        with open(csv_,encoding=encoding) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=delimiter)
            for row in csv_reader:
                if self.line_count == 0:
                    self.campos = row
                else:
                    self.datos.append(row)
                self.line_count +=1
            # print number of lines of the csv
            Log.logger.info('\tLineas      :'+str(self.line_count))
            # print fields of the csv
            Log.logger.info('\tCampos      :'+str(self.campos))
