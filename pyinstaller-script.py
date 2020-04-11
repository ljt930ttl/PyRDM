#!/usr/bin/env python
# -*- coding: utf-8 -*-
# EASY-INSTALL-ENTRY-SCRIPT: 'PyInstaller==3.3.1','console_scripts','pyinstaller'
__requires__ = 'PyInstaller==3.6'
import re
import sys
from pkg_resources import load_entry_point

import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    #,'-i ./ico/cloud_logo.ico'
    opts=['main.py','-w','-F' ,'-itool.ico']
    run(opts)
