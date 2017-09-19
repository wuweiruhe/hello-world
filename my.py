#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: eph
import sys, pickle,argparse
from time import time, sleep
import time
from SocketServer import ThreadingMixIn
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urllib import urlopen, urlencode
from urlparse import urlparse, parse_qsl
from threading import Thread

parser=argparse.ArgumentParser(description="mydemo")



parser.add_argument('-c', '--can', metavar = 'PORT', type = int, default = 100,
                    help = 'CAN port of encoder (default = 1)')
parser.add_argument('-o', '--output', metavar = 'FILEww', type = argparse.FileType('wb'), default = None,
                    help = 'output file')


args = parser.parse_args()

if args.can:
   args.output.write("tyyayyaa")
   sys.stdout.write("tuyanannn")







