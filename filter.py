#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Name: Saky
# Mail: sakydogalo@gmail.com
#
# 

import logging
import coloredlogs

from argumentos import Argumentos
from archivo import Archivo
from log import Log
from procesador import Procesador

Log.logger.info("Parámetros entregados:")
Log.logger.info("\t"+str(Argumentos.args))

p = Procesador()

p.abrir(Argumentos.args.csv,Argumentos.args.encoding,Argumentos.args.delimiter)
p.enumerar()
p.guardar('sin-procesar.csv',Argumentos.args.encoding,Argumentos.args.delimiter)
p.guardar_procesado('procesado.csv',Argumentos.args.encoding,Argumentos.args.delimiter)

#
# print(a.campos)
# print(a.line_count)
