#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Name: Saky
# Mail: sakydogalo@gmail.com
#
# 

import argparse

class Argumentos(object):
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
 
    parser.add_argument(
        "csv",
        help="Archivo a procesar",
        type=str)

    parser.add_argument(
        "-e","--encoding", 
        help="Codificación de archivo",
        type=str,
        default='ISO-8859-1')

    parser.add_argument(
        "-d","--delimiter", 
        help="Carácter delimitador",
        type=str,
        default=';')

    parser.add_argument(
        "-o","--order",
        help="Campos a ordenar",
        type=str,
        default='nada')

    args: argparse.Namespace = parser.parse_args()