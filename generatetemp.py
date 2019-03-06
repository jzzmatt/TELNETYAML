#!/usr/bin/env python
from jinja2 import Template
import sys
import yaml
import argparse


class GenerateTemp(object):
    def __init__(self, file_j2):
        with open(file_j2) as f:
            self.template_file = Template(f.read())

        self._template = None

    def load_var(self, file_vars):
        with open(file_vars) as f:
            vars_yml = yaml.load(f.read())
        self._template = self.template_file.render(vars_yml)

    def extract_to_file(self, file_name):
        with open(file_name, "w") as f:
            f.write(self._template)


def main():
    if len(sys.argv) <= 1:
        print("Use {} -h or --help to get script help menu".format(sys.argv[0]))

    else:

        parser = argparse.ArgumentParser()
        parser.add_argument('--j', help="[j] ,load jinja2 file")
        parser.add_argument('--a', help="[a] , load yml variable file")
        parser.add_argument('--o', help="[o] ,export to <filename>")
        args = parser.parse_args()

        # DEPLOY TEMPLATE
        get_j2 = GenerateTemp(args.j)
        get_j2.load_var(args.a)
        get_j2.extract_to_file(args.o)


if __name__ == '__main__':
    main()