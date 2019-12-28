#!/usr/bin/env python3
# Soubor:  jinja-create-config.py
# Datum:   28.12.2019 10:47
# Autor:   Marek Nožka, marek <@t> tlapicka <d.t> net
# Licence: GNU/GPL
############################################################################
import os
import sys
from socket import gethostname
from jinja2 import FileSystemLoader, Environment

# change directory
dirname = os.path.dirname(sys.argv[0])
os.chdir(dirname)


templateLoader = FileSystemLoader(searchpath="./")
templateEnv = Environment(loader=templateLoader)
template = templateEnv.get_template("config.j2")

with open("config", "w") as f:
    f.write(template.render(hostname=gethostname()))
