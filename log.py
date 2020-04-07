#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   
# Name: Saky
# Mail: sakydogalo@gmail.com
#
# 

import logging
import coloredlogs

class Log(object):
    #configuring logger
    coloredlogs.DEFAULT_LOG_FORMAT = '\r%(asctime)s%(levelname)8s%(filename)15s\
    %(lineno)4s: %(message)s'
    coloredlogs.increase_verbosity()
    coloredlogs.install()
    logger = logging.getLogger(__name__)

    def info(self,message):
        self.logger.info(message)
