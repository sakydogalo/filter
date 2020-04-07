#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# convert csv to json file with panda
#

import pandas as pd

def getCSV ():
    global read_file
    import_file_path = 'FACTURACION.csv'
    read_file = pd.read_csv (import_file_path,encoding='ISO-8859-1',delimiter=';',header=0)

def convertToJSON ():
    global read_file
    export_file_path = 'FACTURACION.json'
    read_file.to_json (export_file_path, orient='records',lines=True)

getCSV()
convertToJSON()
