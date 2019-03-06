#!/usr/bin/env python
import yaml

class GetYaml(object):
    def __init__(self, file_yml):
        self.file_yml = file_yml
        self.inventory = None

    def _convert_to_dict(self):
        with open(self.file_yml) as f:
            self.inventory = yaml.load(f.read())

    def get_invent(self):
        self._convert_to_dict()
        return self.inventory

class ParseInvent(object):
    def __init__(self, inventory_file):
        self.inventory = inventory_file

    def get_all_hosts(self):
        hosts_lists = []
        for site_name in self.inventory['site']:
            hosts_lists.extend(self.inventory['site'][site_name]['hosts'])
        return hosts_lists

    def get_site_hosts(self, site_name):
        return self.inventory['site'][site_name]['hosts']