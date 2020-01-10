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
from glob import glob

# change directory
dirname = os.path.dirname(sys.argv[0])
os.chdir(dirname)


templateLoader = FileSystemLoader(searchpath="./")
templateEnv = Environment(loader=templateLoader)

template_files = glob("*.j2")
for template_file in template_files:
    (config_file, ext) = os.path.splitext(template_file)
    template = templateEnv.get_template(template_file)
    with open(config_file, "w") as f:
        f.write(template.render(hostname=gethostname()))
