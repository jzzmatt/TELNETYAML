#!/usr/bin/env python
from getyaml import GetYaml
from getyaml import ParseInvent
from generatetemp import GenerateTemp
from pprint import pprint
from telnet_conn import MyTelConn
import argparse
import sys


def main():
    if len(sys.argv) <= 1:
        print("Use {} -h or --help to get script help menu".format(sys.argv[0]))

    else:
        #DEFINE PARSER
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', help="i [inventory file]")
        parser.add_argument('-t', help="t [configuration file]")
        parser.add_argument('--s', help="[site] inventory hosts")
        args = parser.parse_args()

        # GET INVENTORY
        inventory = GetYaml(args.i).get_invent()
        hostlist = []
        try:
            if args.s == "all":
                hostlist = ParseInvent(inventory).get_all_hosts()
            else:
                hostlist = ParseInvent(inventory).get_site_hosts(args.s)

        except KeyError:
            print("Verify that the site exist in inventory file and try again !!")
            sys.exit()

        #print(hostlist)
        myconn = MyTelConn()

        for host in hostlist:
            myconn.connect(host, 'admin', 'password')
            myconn.sendtemplate(args.t)

if __name__=="__main__":
    main()