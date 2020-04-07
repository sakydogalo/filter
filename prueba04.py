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


Log.logger.info("Parámetros entregados:")
Log.logger.info("\t"+str(Argumentos.args))
a = Archivo()
a.abrir(Argumentos.args.csv,Argumentos.args.encoding,Argumentos.args.delimiter)

#
print(a.campos)
print(a.line_count)
