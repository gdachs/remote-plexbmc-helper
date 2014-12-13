#!/usr/bin/env python

import sys
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("server", help="the name or ip of the Plex Media Server")
parser.add_argument("client", help="the name or ip of the xbmc client")
parser.add_argument("mac", help="the MAC address of the xbmc client")

parser.parse_args()

sys.path.append('script.plexbmc.helper')
sys.path.append('pywakeonlan')
sys.path.append(os.path.join('script.plexbmc.helper', 'resources', 'lib' ))

import default
